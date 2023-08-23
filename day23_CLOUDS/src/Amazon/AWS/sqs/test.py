import os

import boto3
from dotenv import load_dotenv

from app import SQS

load_dotenv()
session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
    region_name=os.getenv('REGION_NAME')
)
client = session.client(
    "sqs",
    endpoint_url="https://sqs.{}.amazonaws.com".format(
        os.environ.get("REGION_NAME"))
)
client.large_payload_support = 'my-bucket-name'
client.always_through_s3 = True
sqs_object = SQS(client)

# print(sqs_object.create_queue('QUEUE_NAME', {
#     'DelaySeconds': '0',
#     'MaximumMessageSize': '262144',
#     'MessageRetentionPeriod': '345600',
#     'ReceiveMessageWaitTimeSeconds': '0',
#     'VisibilityTimeout': '6*60*60',
#     'FifoQueue': 'true'
# }))


print(sqs_object.purge_queue('QUEUE_URL'))
