import json
import time

from requests import get

from day24_SalesforceAPIs.config.urlConfig import version
from day24_SalesforceAPIs.src.authorization import get_access_token


class RESTEXPLORER:  # This is a singleton class
    def __init__(self, env_type):
        self.token = get_access_token(env_type=env_type)
        self.env_type = env_type

    def __token_generator__(self):
        current_time, issued_at = int(time.time()), int(self.token['issued_at'][0:10])
        access_token = self.token["access_token"] if current_time - issued_at < 3500 else \
            get_access_token(env_type=self.env_type)['access_token']
        return access_token

    def object_describe(self, object_name: str):
        url = f'{self.token["instance_url"]}/services/data/v{version}/sobjects/{object_name}/describe'
        headers = {
            'Authorization': f'Bearer {self.__token_generator__()}'
        }
        response = get(url, headers=headers)
        result = json.loads(response.text)
        return result

    def list_org_limits(self):
        url = f'{self.token["instance_url"]}/services/data/v{version}/limits'
        headers = {
            'Authorization': f'Bearer {self.__token_generator__()}'
        }
        response = get(url, headers=headers)
        result = json.loads(response.text)
        return result

    def list_rest_resources(self):
        url = f'{self.token["instance_url"]}/services/data/v{version}'
        headers = {
            'Authorization': f'Bearer {self.__token_generator__()}'
        }
        response = get(url, headers=headers)
        result = json.loads(response.text)
        return result


ab = RESTEXPLORER('sandbox')
print(ab.list_rest_resources())
