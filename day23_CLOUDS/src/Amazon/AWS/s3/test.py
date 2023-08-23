import zipfile
from io import BytesIO

import boto3 as boto3

# Stream data from one S3 t another S3 without saving anything in local
session = boto3.resource('s3', aws_access_key_id="PROVIDE ACCESS KEY",
                         aws_secret_access_key="PROVIDE SECRET ACCESS KEY",
                         aws_session_token="PROVIDE SESSION TOKEN")


def upload_zip_to_s3(bucket_name: str, key_name: str, path: str):
    zip_obj = session.Object(bucket_name=bucket_name, key=key_name) # type: ignore
    buffer = BytesIO(zip_obj.get()["Body"].read())
    z = zipfile.ZipFile(buffer)
    for filename in z.namelist():
        file_info = z.getinfo(filename)
        print(file_info)
        session.meta.client.upload_fileobj(
            z.open(filename, force_zip64=True),  # To Process files which are more than 2 GB.
            Bucket=bucket_name,
            Key=f'{path}/{filename}'
        )


upload_zip_to_s3(bucket_name="orgtools-backup-us-east-1-qamicro",
                 key_name='1001/_ - 2022-05-13 06:01:38/_metadata_backup.zip',
                 path='1001/_ - 2022-05-13 06:01:38/_metadata_backup')

# s3_resource = boto3.resource('s3')

# s3 = S3(client)
# #
#
# # def download_files(bucket_name, src_obj, dest_path):
# #     try:
# #         session.download_file(bucket_name, src_obj, dest_path)
# #         print(" downloading object: %s to %s" % (src_obj, dest_path))
# #     except Exception as e:
# #         print(f'Unable to download files: {e}')
# #         raise e
# #
# #
# # def download_dir(bucket_name, prefix, local_dir):
# #     try:
# #         paginator = session.get_paginator('list_objects_v2')
# #         pages = paginator.paginate(Bucket=bucket_name, Prefix=f'{prefix}/')
# #         pool = Pool(20)  # max_process
# #         mp_data = []
# #         for page in pages:
# #             if 'Contents' in page:
# #                 for obj in page['Contents']:
# #                     src_obj = obj['Key']
# #                     dest_path = local_dir + src_obj
# #                     mp_data.append((bucket_name, src_obj, dest_path))
# #                     os.path.dirname(dest_path) and os.makedirs(os.path.dirname(dest_path), exist_ok=True)
# #         pool.starmap(download_files, mp_data)
# #         return len(mp_data)
# #     except Exception as e:
# #         print(f'Unable to download files: {e}')
# #         raise e
# #
# #
# # def download_multiple_folders(bucket_name, folders, local_dir):
# #     print("starting script...")
# #     start_time = datetime.now()
# #     total_files = 0
# #     for s3_dir in folders:
# #         print("[Information] %s directory is downloading" % s3_dir)
# #         no_files = download_dir(bucket_name, s3_dir, local_dir)
# #         total_files = total_files + no_files
# #
# #     shutil.make_archive(local_dir, 'zip', os.path.dirname(local_dir))
# #     os.remove(os.path.dirname(local_dir))
# #     end_time = datetime.now()
# #     print('Duration: {}'.format(end_time - start_time))
# #     print('Total File numbers: %d' % total_files)
# #     print("ended")
# #
# #
#
import gzip
import io
import json
import os
import shutil
from datetime import datetime
from multiprocessing.pool import Pool

import boto3

max_process = 20  # CAN BE CHANGE
debug_en = True

s3 = boto3.client('s3', aws_access_key_id="Access Key",
                  aws_secret_access_key="Secret Access Key",
                  aws_session_token="")


def download_files(bucket_name, src_obj, dest_path):
    try:
        s3.download_file(bucket_name, src_obj, dest_path)
        if debug_en:
            print("[debug] downloading object: %s to %s" %
                  (src_obj, dest_path))
    except Exception as e:
        print(f'Unable to download files: {e}')
        raise e


def download_dir(bucket_name, sub_prefix, local_dir):
    try:
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=f'{sub_prefix}/')
        pool = Pool(max_process)
        print(pool)
        mp_data = []
        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    src_obj = obj['Key']
                    dest_path = local_dir + src_obj
                    mp_data.append((bucket_name, src_obj, dest_path))
                    os.path.dirname(dest_path) and os.makedirs(
                        os.path.dirname(dest_path), exist_ok=True)
        pool.starmap(download_files, mp_data)
        return len(mp_data)
    except Exception as e:
        print(f'Unable to download files: {e}')
        raise e


def download_folders(bucket_name, folders, local_dir):
    print("...Starting Script...")
    start_time = datetime.now()
    total_files = 0
    for s3_dir in folders:
        print("[Information] %s directory is downloading" % s3_dir)
        no_files = download_dir(bucket_name, s3_dir, local_dir)
        total_files = total_files + no_files

    shutil.make_archive(local_dir, 'zip', os.path.dirname(local_dir))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    print('Total File numbers: %d' % total_files)
    print("ended")
    # with open(f'{os.path.dirname(local_dir)}.zip', 'rb') as f:
    #     data = f.read()
    # response = HttpResponse(data, content_type='application/zip')
    # response['Content-Disposition'] = f'attachment; filename={local_dir}.zip'
    # return response
    # os.remove(os.path.dirname(local_dir))


def get_object(bucket_name: str, filename: str) -> object:
    try:
        response = s3.get_object(
            Bucket=bucket_name,
            SSECustomerAlgorithm=os.getenv('SSE_CUSTOMER_ALGORITHM'),
            SSECustomerKey=os.getenv('SSE_CUSTOMER_KEY'),
            Key=filename
        )
    except Exception as oe:
        print(f'Trying without encryption key:{filename}: {oe}')
        try:
            response = s3.get_object(Bucket=bucket_name, Key=filename)
            with gzip.GzipFile(fileobj=io.BytesIO(response['Body'].read()), mode='rb') as fh:
                return json.load(fh)

        except Exception as e:
            print(
                f'Unable to read data of keyname {filename}: | Exception({e})')
            raise e
    return response

# creating a Flask app
# app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         body = request.get_json(force=True)
#         download_folders(body['bucket_name'], body['folders'], f'./{body["local_dir"]}/')
#     return 'Done'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
# # if __name__ == '__main__':
# download_folders("bucket-name",
#                  ['Folder1', 'Folder2'], './Download/')
#     print("starting script...")
#     start_time = datetime.now()
#     s3_dirs = prefix
#     total_files = 0
#     for s3_dir in s3_dirs:
#         print("[Information] %s directory is downloading" % s3_dir)
#         no_files = download_dir('bucket-name', s3_dir)
#         total_files = total_files + no_files
#
#     shutil.make_archive('Folder1', 'zip', os.path.dirname(local_dir))
#     os.remove(os.path.dirname(local_dir))
#     end_time = datetime.now()
#     print('Duration: {}'.format(end_time - start_time))
#     print('Total File numbers: %d' % total_files)
#     print("ended")
