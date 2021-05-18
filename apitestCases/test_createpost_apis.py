import json

import jsonpath
import requests

url = ""


class testPostAPIRequests:

    def test_create_new_user(self):
        # read input json file
        file = open("../testData/test1JsonData.json", "r")
        json_input = file.read()
        request_json = json.load(json_input)
        # make post request with json input body
        response = requests.post(url, request_json)
        # Validate Response code
        assert response.status_code == 201
        # Fetch headers from response
        print(response.headers.get('Content-Length'))
        # Parse response into json format
        response_json = json.load(response.text)
        # pick Id using json path
        id = jsonpath.jsonpath(response_json, 'id')
        print(id[0])
