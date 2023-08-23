import os

import boto3


class S3MultipartUpload(object):
    # AWS throws EntityTooSmall error for parts smaller than 5 MB
    PART_MINIMUM = int(5e6)

    def __init__(self, bucket, key, local_path, part_size=int(15e6), profile_name=None, region_name='us-east-1',
                 verbose=False):
        self.bucket = bucket
        self.key = key
        self.path = local_path
        self.total_bytes = os.stat(local_path).st_size
        self.part_bytes = part_size
        assert part_size > self.PART_MINIMUM
        assert (self.total_bytes % part_size == 0
                or self.total_bytes % part_size > self.PART_MINIMUM)
        self.s3 = boto3.session.Session(
            profile_name=profile_name, region_name=region_name).client("s3")
        if verbose:
            boto3.set_stream_logger(name="botocore")

    def abort_all(self):
        mpus = self.s3.list_multipart_uploads(Bucket=self.bucket)
        aborted = []
        print("Aborting", len(mpus), "uploads")
        if "Uploads" in mpus:
            for u in mpus["Uploads"]:
                upload_id = u["UploadId"]
                aborted.append(
                    self.s3.abort_multipart_upload(
                        Bucket=self.bucket, Key=self.key, UploadId=upload_id))
        return aborted

    def create(self):
        mpu = self.s3.create_multipart_upload(Bucket=self.bucket, Key=self.key)
        mpu_id = mpu["UploadId"]
        return mpu_id

    def upload(self, mpu_id):
        parts = []
        uploaded_bytes = 0
        with open(self.path, "rb") as f:
            i = 1
            while True:
                # Read data from file or provide data stream
                data = f.read(self.part_bytes)
                if not len(data):
                    print("No data read from file")
                    break
                part = self.s3.upload_part(
                    Body=data, Bucket=self.bucket, Key=self.key, UploadId=mpu_id, PartNumber=i,
                    SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                    SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
                )
                parts.append({"PartNumber": i, "ETag": part["ETag"]})
                uploaded_bytes += len(data)
                print("{0} of {1} uploaded ({2:.3f}%)".format(
                    uploaded_bytes, self.total_bytes,
                    as_percent(uploaded_bytes, self.total_bytes)))
                i += 1
        return parts

    def complete(self, mpu_id: int, parts) -> object:
        try:
            result = self.s3.complete_multipart_upload(
                Bucket=self.bucket,
                Key=self.key,
                UploadId=mpu_id,
                MultipartUpload={"Parts": parts},
                SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
            )
            return result
        except Exception as e:
            print("Error completing upload:", e)
            print("Aborting upload")
            self.s3.abort_multipart_upload()
            print("Aborted upload")
            return None


# Helper
def as_percent(num: int, denominator: int) -> float:
    return float(num) / float(denominator) * 100.0


def main():
    mpu = S3MultipartUpload(
        'Bucket-name',
        'fileName1',
        'fileName2',
        profile_name='default',
        region_name='us-east-1')
    # abort all multipart uploads for this bucket (optional, for starting over)
    # mpu.abort_all()
    # create new multipart upload
    mpu_id = mpu.create()
    # upload parts
    parts = mpu.upload(mpu_id)
    # complete multipart upload
    print(mpu.complete(mpu_id, parts))


if __name__ == "__main__":
    main()
