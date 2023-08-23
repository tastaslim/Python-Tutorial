import os

import requests
from dotenv import load_dotenv

# from src.Base.Authenticator import Authenticator
# # from src.Microsoft.Dynamics365.d365_token import MicrosoftAuthenticator
# #
# # token = Authenticator(MicrosoftAuthenticator()).access_token(tenant_id="6748a81a-7786-4d6b-9f02-309000866dd7",
# #                                                              resource="https://orgcf18a81f.crm8.dynamics.com")
load_dotenv()


class Dynamics365:
    def __init__(self):
        pass

    @staticmethod
    def get_object(**kwargs):
        """
        @brief Get account from Dynamics 365
        :param kwargs:
        :return:
        """
        try:
            url = f"{kwargs.get('resource')}/api/data/{os.getenv('API_VERSION')}/{kwargs.get('object')}"
            headers = {
                'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}",
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
            response = requests.get(url, headers=headers).json()
            return response.get("value")
        except Exception as e:
            print("Error getting account:", e)
            raise e

    @staticmethod
    def create_object(**kwargs):
        """
        @brief Create account in Dynamics 365
        :param kwargs: resource, payload, object
        :return:
        """
        try:
            url = f"{kwargs.get('resource')}/api/data/{os.getenv('API_VERSION')}/{kwargs.get('object')}"
            headers = {
                'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}",
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
            response = requests.post(url, data=kwargs.get('payload'), headers=headers)
            return response  # .json().get("value")
        except Exception as e:
            print("Error getting account:", e)
            raise e


# res = Dynamics365().get_object(tenant_id="tenant_id", object='object_name',
#                                resource="crm_url")
# print(res)

res = Dynamics365().get_object(tenant_id="tenant_id", object='object_name',
                               resource="crm_url")
print(res)
