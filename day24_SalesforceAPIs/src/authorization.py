import json
import os

import requests


def get_access_token(**payload):
    env_type = payload['env_type']
    login_uri = f'https://{"login" if env_type == "prod" else "test"}.salesforce.com/services/oauth2/token'
    client_id, client_secret = os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET')
    grant_type = 'authorization_code' if payload.get('code') else 'password'
    body = {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'username': os.getenv('USER'),
        'password': os.getenv('PASSWORD')
    }
    response = requests.request("POST", login_uri, data=body).text
    result = json.loads(response)
    return {'access_token': result['access_token'], 'instance_url': result['instance_url'],
            'issued_at': result['issued_at']}
