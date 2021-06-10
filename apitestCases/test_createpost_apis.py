import json

import jsonpath
import pytest
import requests

from apiUtilities.requestUtilities import RequestUtility

url = ""


class testPostAPIRequests:

    @pytest.mark.tcid10
    def test_GetNexusByAddress_TCID_0001(self):
        print("TEST: Post - Get Nexus By Address")
        # create payload
        # read input json file
        file = open("../testData/NexusByAddress.json", "r")
        json_input = file.read()
        request_json = json.load(json_input)

        endpoint = "api/v2/companies/1435173/nexus/byaddress"

        # make the call
        req_obj = RequestUtility()
        response=req_obj.POST(endpoint, request_json)

        # import pdb;
        # pdb.set_trace()

        # verify status code of the call
        assert response.status_code == 201
        # Fetch headers from response
        print(response.headers.get('Content-Length'))
        # Parse response into json format
        response_json = json.load(response.text)
        # pick Id using json path
        Id = jsonpath.jsonpath(response_json, 'id')
        print(Id[0])

        # verify email in the response

        # verify customer is created is database


