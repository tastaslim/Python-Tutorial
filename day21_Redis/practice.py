from datetime import timedelta

import redis
import requests

r = redis.Redis(host='localhost', port=6379, db=0)
base_url = 'https://www.breakingbadapi.com/api'


def get_all_characters():
    uri = f'{base_url}/characters'
    if r.exists('characters'):
        print('Characters already in cache')
        return r.get('characters')
    headers = {'Content-Type': 'application/json'}
    response = requests.get(uri, headers=headers)
    r.set('characters', response.text)
    r.expire('characters', timedelta(seconds=50))
    return response.json()


print(get_all_characters())
