import os

import requests
from dotenv import load_dotenv
from msal import ConfidentialClientApplication

from day23_CLOUDS.src.Base.Authenticator import Authenticator

load_dotenv()


class MicrosoftAuthenticator(Authenticator):
    def __init__(self):
        super().__init__(self)

    def access_token(self, **kwargs) -> dict:
        """
        @brief Get access token from Microsoft
        :param kwargs: tenant_id, resource
        :return: Access Token body
        """
        if kwargs.get("tenant_id") is None or kwargs.get("resource") is None:
            raise ValueError("tenant_id and resource are required")

        url = f'https://login.windows.net/{kwargs.get("tenant_id")}/oauth2/token'
        payload = {
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'resource': kwargs.get("resource"),
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, data=payload)
        return response.json()

    def refresh_token(self, **kwargs) -> dict:
        """
        @brief Refresh access token from Microsoft
        :param kwargs: tenant_id, resource, refresh_token
        :return: Access Token body
        """
        if kwargs.get("tenant_id") is None or kwargs.get("scope") is None or kwargs.get("refresh_token") is None:
            raise ValueError("tenant_id, refresh_token and scope are required")

        url = f'https://login.microsoftonline.com/{kwargs.get("tenant_id")}/oauth2/token'
        payload = {
            'client_id': os.getenv('CLIENT_ID'),
            'client_secret': os.getenv('CLIENT_SECRET'),
            'scopes': [kwargs.get('scope')],
            'grant_type': 'refresh_token',
            'refresh_token': kwargs.get("refresh_token")
        }

        response = requests.post(url, data=payload)
        return response.json()

    @staticmethod
    def build_authorization_url(**kwargs) -> dict:
        """
        @brief Get access token from Microsoft using MSAL
        :param kwargs: tenant_id, resource
        :return: Access Token body
        """
        if kwargs.get("tenant_id") is None or kwargs.get("resource") is None:
            raise ValueError("tenant_id and resource are required")

        app = ConfidentialClientApplication(
            os.getenv('CLIENT_ID'),
            authority=f'https://login.microsoftonline.com/{kwargs.get("tenant_id")}',
            client_credential=os.getenv('CLIENT_SECRET')
        )

        result = app.get_authorization_request_url(scopes=[kwargs.get("resource")],
                                                   redirect_uri='http://localhost:3050',
                                                   prompt="consent", state="state")
        return result

    @staticmethod
    def get_token_from_code(**kwargs) -> dict:
        """
        @brief Get access token from Microsoft using MSAL
        :param kwargs: tenant_id, resource
        :return: Access Token body
        """
        if kwargs.get("tenant_id") is None or kwargs.get("resource") is None or kwargs.get("code") is None:
            raise ValueError("tenant_id, code and resource are required")

        app = ConfidentialClientApplication(
            os.getenv('CLIENT_ID'),
            authority=f'https://login.microsoftonline.com/{kwargs.get("tenant_id")}',
            client_credential=os.getenv('CLIENT_SECRET')
        )

        result = app.acquire_token_by_authorization_code(kwargs.get("code"), scopes=[kwargs.get("resource")],
                                                         redirect_uri='http://localhost:3050')
        return result
