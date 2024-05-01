import json
import os

from requests import get, post
from xmltodict import parse


class Dynamics365:
    def __init__(self):
        self.tenantUrl = os.getenv("tenantUrl")
        self.token = self.__refresh_token()
        self.accessToken = self.token.get("access_token")

    def __refresh_token(self) -> dict:
        url = f'https://login.microsoftonline.com/9b752bd6-12ce-4e59-b789-d1cb1856f4ba/oauth2/token'
        payload = {
            "client_id": os.getenv("clientId"),
            "client_secret": os.getenv("clientSecret"),
            'resource': self.tenantUrl,
            'grant_type': 'refresh_token',
            'refresh_token': os.getenv('refreshToken'),
        }

        response = post(url, data=payload)
        return response.json()

    def listRecords(self, objectName: str):
        url = f"https://{self.tenantUrl}/api/data/v9.2/{objectName}s"
        headers = {
            "Authorization": f"Bearer {self.accessToken}",
            "Content-Type": "application/json"
        }
        response = get(url=url, headers=headers)
        return response.json()

    def getRecord(self, objectName: str, recordId: str):
        url = f"https://{self.tenantUrl}/api/data/v9.2/{objectName}s({recordId})"
        headers = {
            "Authorization": f"Bearer {self.accessToken}",
            "Content-Type": "application/json"
        }
        response = get(url=url, headers=headers)
        return response.json()

    def createRecord(self, objectName: str, payload: dict):
        url = f"https://{self.tenantUrl}/api/data/v9.2/{objectName}s"
        headers = {
            "Authorization": f"Bearer {self.accessToken}",
            "Content-Type": "application/json"
        }
        response = post(url=url, headers=headers, data=json.dumps(payload))
        data = response.text
        return data

    def orgDescribe(self):
        url = f"https://{self.tenantUrl}/api/data/v9.2/$metadata"
        headers = {
            "Authorization": f"Bearer {self.accessToken}"
        }
        response = get(url=url, headers=headers)
        data = parse(response.text)
        return data


dynamics = Dynamics365()
"""
objectName ==> account, contact, lead, opportunitie
"""
# accounts = dynamics.listRecords(objectName='account')
# account = dynamics.getRecord(objectName='account', recordId='ff93ecee-a2af-ee11-a569-6045bd72a53b')
createAccountPayload = {
    'paymenttermscode': 1,
    'industrycode': 1,
    'address2_addresstypecode': 1,
    'merged': False,
    'statecode': 0,
    'exchangerate': 1.0,
    'address1_composite': 'HYD\r\nPUNE\r\nHPAPA\r\nHYD, AHAUAI 500081\r\nLALALA',
    'ownershipcode': 1,
    'websiteurl': 'https://linkedin.com',
    'opendeals': 0,
    'address1_shippingmethodcode': 5,
    'openrevenue_state': 1,
    'donotpostalmail': False,
    'accountratingcode': 1,
    'numberofemployees': 230,
    'marketingonly': False,
    'revenue_base': 272891901.0,
    'preferredcontactmethodcode': 1,
    'description': 'This is My Team',
    'sic': '12345',
    'name': 'Logitech Monitor',
    'tickersymbol': 'TSA',
    'openrevenue_date': '2024-01-10T11:52:45Z',
    'openrevenue_base': 0.0,
    'address1_line1': 'HYD',
    'address1_line2': 'PUNE',
    'address1_line3': 'HPAPA',
    'creditonhold': False,
    'telephone1': '89191919191',
    'donotphone': False,
    'address1_freighttermscode': 1,
    'businesstypecode': 1,
    'donotemail': False,
    'opendeals_state': 1,
    'address2_shippingmethodcode': 1,
    'revenue': 272891901.0,
    'msdyn_gdproptout': False,
    'address2_freighttermscode': 1,
    'statuscode': 1,
    'createdon': '2024-01-10T10:28:06Z',
    'creditlimit': 5261891.0,
    'address1_stateorprovince': 'AHAUAI',
    'openrevenue': 0.0,
    'donotsendmm': False,
    'donotfax': False,
    'donotbulkpostalmail': False,
    'address1_country': 'LALALA',
    'versionnumber': 4732471,
    'donotbulkemail': False,
    'creditlimit_base': 5261891.0,
    'followemail': True,
    'shippingmethodcode': 1,
    'address1_city': 'HYD',
    'territorycode': 1,
    'fax': 'yuiuo',
}

# getOrgDescribe = dynamics.orgDescribe()
listAccounts = dynamics.listRecords(objectName='account')
# getAccount = dynamics.getRecord(objectName='account', recordId='')
# createAccount = dynamics.createRecord(objectName='account', payload=createAccountPayload)
print(listAccounts)
# print(getAccount)
