import json
import os
from requests.auth import HTTPBasicAuth
import jsonpath
import requests
import os
from requests_oauthlib import OAuth1


class RequestUtility(object):

    def __init__(self):
        # self.env = os.environ.get('ENV', 'test')
        self.base_url = 'https://api.qa.avalara.io'  # read from baseclass
        self.auth = HTTPBasicAuth('CalcRegression', 'Qaonly1234$')
        # self.auth = OAuth1("", "")

    def GET(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        rs_api = requests.get(url=self.url, data=json.dump(payload), headers=headers, auth=self.basic_auth)
        status_code = rs_api.status_code
        expected_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json

    def POST(self, endpoint, payload=None, headers=None, expected_status_code=None):

        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        try:
            # rs_api = requests.post(url=url, data=payload, headers=headers, auth=self.auth)
            rs_api = requests.post(url=url, data=payload, headers=headers, auth=self.auth)
            print(rs_api)
            # status_code = rs_api.status_code
            # exp_status_code = expected_status_code
            # rs_json = rs_api.json()
            # self.assert_status_code()
        except Exception as ex:
            print(ex)

        return self.rs_json

    def PUT(self, endpoint, payload=None, headers=None, expected_status_code=None):

        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        rs_api = requests.put(url=url, data=payload, headers=headers, auth=self.auth)
        status_code = rs_api.status_code
        exp_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json

    def DELETE(self, endpoint, payload=None, headers=None, expected_status_code=None):

        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint

        rs_api = requests.delete(url=url, data=payload, headers=headers, auth=self.auth)
        status_code = rs_api.status_code
        exp_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json

    def assert_status_code(self, actual_status_code, expected_status_code):
        pass
