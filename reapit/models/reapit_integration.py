from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError
import requests
from urllib import request, parse
import json, urllib

class ReapitIntegration(models.Model):
    _name = 'reapit.integration'
    _description = 'Reapit Integration'

    def getToken(self):
        url = "https://connect.reapit.cloud/token"
        payload='client_id=q1via61m5a39r2re09i1bsk0n&grant_type=client_credentials'
        headers = {
        'Authorization': 'Basic cTF2aWE2MW01YTM5cjJyZTA5aTFic2swbjoxaXFqYmUyYmlkdG51a3EzcDJnbjh2OGtvcnRmNjdkZzFtZjE4MWNibzBxY3FyZW9jdDY0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'XSRF-TOKEN=204806c6-be20-42b8-ad06-c2ee5cfd454e'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        obj = json.loads(response.text)
        token = obj['access_token']
        return token

    def getData(self,api_version,url):
        import requests
        #url = "https://platform.reapit.cloud/offers/?PageNumber=7&PageSize=2000"
        token = self.getToken()
        payload={}
        headers = {
        'reapit-customer': 'HAH',
        'api-version': api_version,
        'Authorization': f'Bearer {token}'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        return data
    
    def getHappyTenantData(self,url,apiToken):
        payload={}
        headers = {
            'Authorization': apiToken
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        return data


# if __name__ == "__main__":
#     token = ReapitIntegration().getData('https://happytenant.app/api/payments/list?start_date=01-01-2020&end_date=01-01-2021',"ht_live_io3LEXLsnPQoipk6PqvnQQ==")
#     print(token)
