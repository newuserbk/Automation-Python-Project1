import json
import jsonpath
import requests
from apiUtilities.requestUtilities import RequestUtility


class TestGetAPIRequests(object):

    def test_GetCompanyDetails_TCID0002(self):
        print("TEST: Post - Get Company Details")
        endpoint = "api / v2 / companies / 1435173"

        # make the call
        req_obj = RequestUtility()
        response = req_obj.GET(endpoint)

        # import pdb;
        # pdb.set_trace()

        # verify status code of the call
        assert response.status_code == 200
        # Fetch headers from response
        print(response.headers.get('Content-Length'))
        # Parse response into json format
        response_json = json.load(response.text)
        # pick Id using json path
        Id = jsonpath.jsonpath(response_json, 'id')
        print(Id[0])

        # verify email in the response

        # verify customer is created is database

