import json
import unittest

import jsonpath
import pytest
import requests

from apiUtilities.requestUtilities import RequestUtility
from helpers.JsconHelper import ReadJsonUtility


class test_PostAPIRequests:

    @pytest.mark.tcid10
    def GetNexusByAddress_TCID_tests(self):
        print("TEST: Post - Get Nexus By Address")
        # create payload
        request_json=ReadJsonUtility.read_json_file()

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


