import json

import requests


class CredentialUtility(object):
    def __init__(self):
        pass

    @staticmethod
    def get_key_and_secret():
        clientId="" # read from base class
        clientSecret="" # read from base class or config
        if not clientId or not clientSecret:
            raise Exception("The API credentials 'ClientId' and 'ClientSecret' must be config/environment variable ")
        else:
            return {'Client_Id':clientId,'Client_Secret':clientSecret}

    @staticmethod
    def get_access_Token(clientId,clientSecret,token_url):
        token_url = "https://api.byu.edu/token"
        test_api_url = "<<url of the api you want to call goes here>>"

        client_id = '<<client_id goes here>>'
        client_secret = '<<client_secret goes here>>'

        # step B, C - single call with resource owner credentials in the body
        # and client credentials as the basic auth header
        # will return access_token

        data = {'grant_type': 'password', 'username': 'CalcRegression', 'password': 'Qaonly1234$'}

        access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False,
                                              auth=(client_id, client_secret))

        print("Access Token response headers : "+ access_token_response.headers)
        print("Access Token Response text : "+access_token_response.text)

        tokens = json.loads(access_token_response.text)
        print("Access Token Value : "+ tokens['access_token'])

        return tokens['access_token']


