import json

import jsonpath
import requests

url = ""


class testGetAPIRequests:

    def get_main_url(self):
        return url


    def test_valid_login(self,get_main_url):
        url=self.get_main_url()+'/api/login/'
        data={'username':'bharat','password':'test123'}
        # make get request
        response = requests.get(url, data=data)
        # Validate Response code
        assert response.status_code == 200
        # Fetch headers from response
        print(response.headers.get('Content-Length'))
        print(response.content)
        # Parse response into json format
        response_json = json.load(response.text)

