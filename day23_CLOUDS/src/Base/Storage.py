"""
@class BaseStorage
@brief Base class for all storage classes such as AWS, Azure Active Directory, GCP etc.
"""


class BaseStorage:
    def __init__(self, client_name):
        self.client_name = client_name

    def list_buckets(self):
        try:
            return self.client_name.list_buckets()
        except NotImplementedError as e:
            print("Error listing buckets:", e)
            raise e

    def get_bucket(self, bucket_name):
        self.client_name.get_bucket(bucket_name)

    def delete_bucket(self, bucket_name):
        self.client_name.delete_bucket(bucket_name)

    def create_bucket(self, bucket_name):
        self.client_name.create_bucket(bucket_name)

    def update_bucket(self, bucket_name, new_bucket_name):
        self.client_name.update_bucket(bucket_name, new_bucket_name)

    def list_objects(self, bucket_name):
        self.client_name.list_objects(bucket_name)

    def read_object(self, bucket_name, key):
        self.client_name.read_object(bucket_name, key)

    def upload_object(self, bucket_name, key, content):
        self.client_name.upload_object(bucket_name, key, content)

    def download_object(self, bucket_name, key, filename):
        self.client_name.download_object(bucket_name, key, filename)

    def delete_object(self, bucket_name, key):
        self.client_name.delete_object(bucket_name, key)

    def query_objects(self, bucket_name, key, query):
        self.client_name.query_objects(bucket_name, key, query)
