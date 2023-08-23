import logging

from dotenv import load_dotenv

load_dotenv()
logging = logging.getLogger()
logging.setLevel(20)  # 20 = logging.INFO


class SQS:
    def __init__(self, client_name):
        self.client_name = client_name

    def list_queues(self, queue_name_prefix: str = '', next_token: str = '', max_results: int = 1000):
        response = []
        try:
            if max_results > 1000:
                if next_token:
                    paginated_response = self.client_name.list_queues(
                        QueueNamePrefix=queue_name_prefix,
                        NextToken=next_token,
                        MaxResults=max_results
                    )
                else:
                    paginated_response = self.client_name.list_queues(
                        QueueNamePrefix=queue_name_prefix,
                        MaxResults=max_results
                    )
                response.extend(paginated_response['QueueUrls'])

                next_page_token = paginated_response.get('NextToken')
                while next_page_token in paginated_response:
                    paginated_response = self.client_name.list_queues(
                        QueueNamePrefix=queue_name_prefix,
                        NextToken=paginated_response['NextToken'],
                        MaxResults=max_results
                    )
                    next_page_token = paginated_response.get('NextToken')
                    response.extend(paginated_response['QueueUrls'])
            else:
                if next_token:
                    paginated_response = self.client_name.list_queues(
                        QueueNamePrefix=queue_name_prefix,
                        NextToken=next_token,
                        MaxResults=max_results
                    )
                else:
                    paginated_response = self.client_name.list_queues(
                        QueueNamePrefix=queue_name_prefix,
                        MaxResults=max_results
                    )
                response.extend(paginated_response['QueueUrls'])

            return response
        except Exception as e:
            print("Error listing queues:", e)
            raise e

    def create_queue(self, queue_name: str, attributes: dict = None):
        try:
            response = self.client_name.create_queue(
                QueueName=queue_name,
                Attributes=attributes
            )
            return response
        except Exception as e:
            print("Error creating queue:", e)
            raise e

    def delete_queue(self, queue_url: str):
        try:
            response = self.client_name.delete_queue(
                QueueUrl=queue_url
            )
            return response
        except Exception as e:
            print("Error deleting queue:", e)
            raise e

    def get_queue_attributes(self, queue_url: str, attribute_names: list = None):
        try:
            response = self.client_name.get_queue_attributes(
                QueueUrl=queue_url,
                AttributeNames=attribute_names
            )
            return response
        except Exception as e:
            print("Error getting queue attributes:", e)
            raise e

    def set_queue_attributes(self, queue_url: str, attributes: dict):
        try:
            response = self.client_name.set_queue_attributes(
                QueueUrl=queue_url,
                Attributes=attributes
            )
            return response
        except Exception as e:
            print("Error setting queue attributes:", e)
            raise e

    def send_message(self, queue_url: str, message_body: str, delay_seconds: int = 0, message_attributes: dict = None):
        try:
            response = self.client_name.send_message(
                QueueUrl=queue_url,
                MessageBody=message_body,
                DelaySeconds=delay_seconds,
                MessageAttributes=message_attributes
            )
            return response
        except Exception as e:
            print("Error sending message:", e)
            raise e

    def send_message_batch(self, queue_url: str, entries: list):
        try:
            response = self.client_name.send_message_batch(
                QueueUrl=queue_url,
                Entries=entries
            )
            return response
        except Exception as e:
            print("Error sending message batch:", e)
            raise e

    def receive_message(self, queue_url: str, attribute_names: list = None, message_attribute_names: list = None,
                        max_number_of_messages: int = 1, visibility_timeout: int = 30, wait_time_seconds: int = 0):
        try:
            response = self.client_name.receive_message(
                QueueUrl=queue_url,
                AttributeNames=attribute_names,
                MessageAttributeNames=message_attribute_names,
                MaxNumberOfMessages=max_number_of_messages,
                VisibilityTimeout=visibility_timeout,
                WaitTimeSeconds=wait_time_seconds
            )
            return response
        except Exception as e:
            print("Error receiving message:", e)
            raise e

    def delete_message(self, queue_url: str, receipt_handle: str):
        try:
            response = self.client_name.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            return response
        except Exception as e:
            print("Error deleting message:", e)
            raise e

    def delete_message_batch(self, queue_url: str, entries: list):
        try:
            response = self.client_name.delete_message_batch(
                QueueUrl=queue_url,
                Entries=entries
            )
            return response
        except Exception as e:
            print("Error deleting message batch:", e)
            raise e

    def purge_queue(self, queue_url: str):
        try:
            response = self.client_name.purge_queue(
                QueueUrl=queue_url
            )
            return response
        except Exception as e:
            print("Error purging queue:", e)
            raise e
