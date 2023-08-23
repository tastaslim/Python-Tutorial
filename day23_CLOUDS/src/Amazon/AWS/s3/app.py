import json
import math
import os
import shutil
from datetime import datetime
from multiprocessing.pool import Pool
from time import time

from boto3.s3.transfer import TransferConfig
from dotenv import load_dotenv

import multipart as multipart
from day23_CLOUDS.src.Base.Storage import BaseStorage

config = TransferConfig(multipart_threshold=1024 * 25,  # Limit it to 25 MB
                        max_concurrency=10,
                        multipart_chunksize=1024 * 25,
                        use_threads=True)  # Use 10 threads
# import pandas as pd
# from src.Base.storage import BaseStorage

load_dotenv()


class S3(BaseStorage):
    def __init__(self, client_name):
        super().__init__(client_name)
        self.client_name = client_name

    @staticmethod
    def convert_size(size_bytes: int) -> str:
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    @staticmethod
    def __get_chunks(size_bytes: int, desired_sections: int) -> int:
        return size_bytes // desired_sections

    def list_buckets(self) -> list:
        try:
            response = self.client_name.list_buckets()
            buckets = []
            for bucket in response['Buckets']:
                buckets.append(bucket['Name'])
            return buckets
        except Exception as e:
            print(f'Unable to list all buckets: {e}')
            raise e

    def create_bucket(self, bucket_name: str, region: str = 'us-east-1') -> dict:
        try:
            response = self.client_name.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
            return response
        except Exception as e:
            print(f'Unable to create bucket: {e}')
            raise e

    def get_object(self, bucket_name: str, filename: str) -> dict:
        try:
            response = self.client_name.get_object(
                Bucket=bucket_name,
                SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                SSECustomerKey=os.getenv('SSE_CUSTOMER_ KEY'),
                Key=filename
            )
        except Exception as oe:
            print(f'Trying without encryption key:{filename}: {oe}')
            try:
                response = self.client_name.get_object(Bucket=bucket_name, Key=filename)
            except Exception as e:
                print(f'Unable to read data of keyname {filename}: | Exception({e})')
                raise e
        return response

    def download_file_custom(self, bucket_name: str, key: str, filename: str) -> None:
        try:
            response = self.client_name.download_file(Bucket=bucket_name, Key=key, Filename=filename,
                                                      ExtraArgs={
                                                          'SSECustomerAlgorithm': os.getenv('SSE_CUSTOMER_ALGORITHM'),
                                                          'SSECustomerKey': os.getenv('SSE_CUSTOMER_KEY')
                                                      })
            return response
        except Exception as oe:
            print(f'Trying without encryption key:{filename}: {oe}')
            try:
                self.client_name.download_file(Bucket=bucket_name, Key=key, Filename=filename)
            except Exception as ie:
                print(f'Unable to read data of keyname {filename}: | Exception({ie})')
                raise ie

    def delete_bucket(self, bucket_name: str) -> None:
        try:
            response = self.client_name.delete_bucket(Bucket=bucket_name)
            return response
        except Exception as e:
            print(f'Unable to delete bucket: {e}')
            raise e

    def query_objects(self, bucket_name: str, key: str, query: str) -> None:
        try:
            resp = self.client_name.select_object_content(
                Bucket=bucket_name,
                Key=key,
                SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
                Expression=query,
                ExpressionType='SQL',
                InputSerialization={
                    'JSON': {
                        'Type': 'DOCUMENT'
                    }, 'CompressionType': 'GZIP'
                },
                OutputSerialization={
                    'JSON': {
                        'RecordDelimiter': ','
                    }
                }
            )
            # return response
        except Exception as oe:
            print(f'Trying without encryption key | Exception({oe})')
            try:
                resp = self.client_name.select_object_content(
                    Bucket=bucket_name,
                    Key=key,
                    Expression=query,
                    ExpressionType='SQL',
                    InputSerialization={
                        'CompressionType': 'GZIP',
                        'JSON': {
                            'Type': 'DOCUMENT'
                        }
                    },
                    OutputSerialization={
                        'JSON': {
                            'RecordDelimiter': ','
                        }
                    }
                )
                # return response
            except Exception as ie:
                print(f'Unable to query objects: {ie}')
                raise ie

        with open('s3-select-data', 'a+') as filtered_file:
            for record in resp['Payload']:
                if 'Records' in record:
                    res = record['Records']['Payload'].decode('utf-8')
                    filtered_file.write(res)

    def multipart_upload(self, bucket_name: str, key: str, file_path: str, region_name: str = 'us-east-1') -> None:
        s3_multipart_upload = multipart.S3MultipartUpload(bucket_name, key, file_path, self.client_name,
                                                          profile_name='default',
                                                          region_name=region_name)
        try:
            upload_id = s3_multipart_upload.create()
            parts = s3_multipart_upload.upload(upload_id)
            print(s3_multipart_upload.complete(upload_id, parts))
        except Exception as e:
            print("Error completing upload:", e)
            print("Aborting upload")
            s3_multipart_upload.abort_all()
            print("Aborted upload")
            return None

    def s3_get_meta_data(self, bucket_name: str, key: str) -> dict:
        meta_data = self.client_name.head_object(Bucket=bucket_name, Key=key)
        return meta_data

    def s3_large_download(self, bucket: str, key: str, parallel_threads: int) -> None:
        start = time()
        md = self.s3_get_meta_data(bucket, key)
        chunk = self.__get_chunks(md["ContentLength"], parallel_threads)
        print("Making %s parallel s3 calls with a chunk size of %s each..." % (
            parallel_threads, self.convert_size(chunk)))
        self.client_name.download_file(
            Bucket=bucket,
            Filename=key.split("/")[-1],  # Provide your path to download the file
            Key=key,
            Config=config,
            SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
            SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY')
        )
        end = time() - start
        print("Finished downloading %s in %s seconds" % (key, end))

    def s3_select_large_files(self, bucket_name: str, key: str, query: str) -> None:
        md = self.s3_get_meta_data(bucket_name, key)
        file_size = md["ContentLength"]
        print(file_size)
        chunk = 15212  # 5KB chunk
        start_range = 0
        end_range = min(chunk, file_size)
        # response = []
        try:
            while start_range < file_size:
                resp = self.client_name.select_object_content(
                    Bucket=bucket_name,
                    Key=key,
                    Expression=query,
                    SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                    SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
                    ExpressionType='SQL',
                    RequestProgress={
                        'Enabled': True | False
                    },
                    InputSerialization={
                        'CompressionType': 'GZIP',
                        'JSON': {
                            'Type': 'DOCUMENT'
                        }
                    },
                    OutputSerialization={
                        'JSON': {
                            'RecordDelimiter': ','
                        }
                    },
                    ScanRange={
                        'Start': start_range,
                        'End': end_range
                    }
                )
                with open('s3-select-data', 'a+') as filtered_file:
                    for record in resp['Payload']:
                        if 'Records' in record:
                            res = record['Records']['Payload'].decode('utf-8')
                            filtered_file.write(res)
                start_range = end_range
                end_range = end_range + min(chunk, file_size - end_range)
        except Exception as oe:
            print(f'Trying without encryption key | Exception({oe})')
            try:
                while start_range < file_size:
                    resp = self.client_name.select_object_content(
                        Bucket=bucket_name,
                        Key=key,
                        Expression=query,
                        ExpressionType='SQL',
                        RequestProgress={
                            'Enabled': True | False
                        },
                        InputSerialization={
                            'CSV': {
                                'FileHeaderInfo': 'USE',
                                'FieldDelimiter': ',',
                                'RecordDelimiter': '\n'
                            }
                        },
                        OutputSerialization={
                            'JSON': {
                                'RecordDelimiter': ','
                            }
                        },
                        # ScanRange is not supported for InputSerialization ==> CompressionType = GZIP and JSON.Type
                        # = DOCUMENT
                        ScanRange={
                            'Start': start_range,
                            'End': end_range
                        }
                    )
                    with open('s3-select-data.csv', 'a+') as filtered_file:
                        for record in resp['Payload']:
                            if 'Records' in record:
                                res = record['Records']['Payload'].decode('utf-8')
                                filtered_file.write(res)

                    start_range = end_range
                    end_range = end_range + min(chunk, file_size - end_range)
            except Exception as ie:
                print(f'Unable to query objects: {ie}')
                raise ie

    def s3_select_multiple_files(self, bucket_name: str, query: str, pfx: str, dlm: str, start: object) -> None:
        try:
            final_count = 0
            pfx = pfx[1:] if pfx.startswith(dlm) else pfx
            start = (start or pfx) if pfx.endswith(dlm) else start
            s3_paginator = self.client_name.get_paginator('list_objects_v2')
            for page in s3_paginator.paginate(Bucket=bucket_name, Prefix=pfx, StartAfter=start):
                for content in page.get('Contents', ()):
                    key = content['Key']
                    print(f'Querying object: {key}')
                    resp = self.client_name.select_object_content(
                        Bucket=bucket_name,
                        Key=key,
                        Expression=query,
                        ExpressionType='SQL',
                        SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                        SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
                        RequestProgress={
                            'Enabled': True | False
                        },
                        InputSerialization={
                            'JSON': {
                                'Type': 'Document',
                            },
                            'CompressionType': 'GZIP'
                        },
                        OutputSerialization={
                            'CSV': {}
                        }
                    )
                    count = 0
                    for record in resp['Payload']:
                        if 'Records' in record:
                            res = record['Records']['Payload'].decode('utf-8')
                            count = res
                    final_count += count
                    print(f'Filename({key}) | IdCount({count})')
                    # with open('s3-select-data.csv', 'a+') as filtered_file:
                    #     for record in resp['Payload']:
                    #         if 'Records' in record:
                    #             res = record['Records']['Payload'].decode('utf-8')
                    #             if first_iteration:
                    #                 headers = self.get_headers(bucket_name, key)
                    #                 filtered_file.write(headers)
                    #                 first_iteration = False
                    #             filtered_file.write(res)
            # filtered_file.write(']}]')
            print(f'Final Record Count({final_count})')
        except Exception as e:
            print(f'Unable to query objects: {e}')
            raise e

    def list_objects_custom(self, bucket: str, pfx: str, dlm: str, start: object) -> list:
        try:
            keys = []
            pfx = pfx[1:] if pfx.startswith(dlm) else pfx
            start = (start or pfx) if pfx.endswith(dlm) else start
            s3_paginator = self.client_name.get_paginator('list_objects_v2')
            for page in s3_paginator.paginate(Bucket=bucket, Prefix=pfx, StartAfter=start):
                for content in page.get('Contents', ()):
                    keys.append(content['Key'])
                print(len(keys))
            return keys
        except Exception as e:
            print(f'Unable to list objects: {e}')
            raise e

    def get_headers(self, bucket: str, key: str) -> str:
        try:
            resp = self.client_name.select_object_content(
                Bucket=bucket,
                Key=key,
                SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
                Expression='SELECT * FROM S3Object s LIMIT 1',
                ExpressionType='SQL',
                RequestProgress={
                    'Enabled': True | False
                },
                InputSerialization={
                    'JSON': {
                        'Type': 'Document',
                    },
                    'CompressionType': 'GZIP'
                },
                OutputSerialization={
                    'JSON': {
                        'RecordDelimiter': ','
                    }
                }
            )
            response = []
            for record in resp['Payload']:
                if 'Records' in record:
                    res = record['Records']['Payload'].decode('utf-8')
                    response.append(res)

            if response and len(response) > 0:
                response = list(json.loads(response[0][:-1]).keys())
                response = ','.join(response)
            return str(response)
        except Exception as e:
            print(f'Unable to get headers: {e}')
            raise e

    def read_index(self, bucket: str, key: str, query) -> int:
        try:
            resp = self.client_name.select_object_content(
                Bucket=bucket,
                Key=key,
                Expression=query,
                ExpressionType='SQL',
                SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
                SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
                RequestProgress={
                    'Enabled': True | False
                },
                InputSerialization={
                    'JSON': {
                        'Type': 'Document',
                    },
                    'CompressionType': 'GZIP'
                },
                OutputSerialization={
                    'JSON': {
                        'RecordDelimiter': ','
                    }
                }
            )
            response = '['
            for record in resp['Payload']:
                if 'Records' in record:
                    res = record['Records']['Payload'].decode('utf-8')
                    # res = f'[{res[0:res.rfind(",")]}'
                    response = response + res
            if response and len(response) > 0:
                if response.endswith(',') and response[-2] == '}':
                    response = response[:-1]
                    response = response + ']'
                else:
                    response = response + '}]'
            response = json.loads(response)

            if response and len(response) > 0:
                response = list(set([item['filename'] for item in response]))
            return len(response)
        except Exception as e:
            print(f'Unable to get headers: {e}')
            raise e

    def download_files(self, bucket_name, src_obj, dest_path):
        try:
            self.client_name.download_file(bucket_name, src_obj, dest_path)
            if True:
                print("[debug] downloading object: %s to %s" % (src_obj, dest_path))
        except Exception as e:
            print(f'Unable to download files: {e}')
            raise e

    def download_dir(self, bucket_name, sub_prefix, local_dir):
        try:
            paginator = self.client_name.get_paginator('list_objects_v2')
            pages = paginator.paginate(Bucket=bucket_name, Prefix=f'{sub_prefix}/')
            pool = Pool(20)
            print(pool)
            mp_data = []
            for page in pages:
                if 'Contents' in page:
                    for obj in page['Contents']:
                        src_obj = obj['Key']
                        dest_path = local_dir + src_obj
                        mp_data.append((bucket_name, src_obj, dest_path))
                        os.path.dirname(dest_path) and os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            pool.starmap(self.download_files, mp_data)
            return len(mp_data)
        except Exception as e:
            print(f'Unable to download files: {e}')
            raise e

    def download_folders(self, bucket_name, folders, local_dir):
        print("starting script...")
        start_time = datetime.now()
        total_files = 0
        for s3_dir in folders:
            print(f"[Information] %{s3_dir} directory is downloading")
            no_files = self.download_dir(bucket_name, s3_dir, local_dir)
            total_files = total_files + no_files

        shutil.make_archive(local_dir, 'zip', os.path.dirname(local_dir))
        os.remove(os.path.dirname(local_dir))
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print('Total File numbers: %d' % total_files)
        print("ended")
