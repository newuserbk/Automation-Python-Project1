import json


class ReadJsonUtility(object):
    @staticmethod
    def read_json_file():
        # read input json file
        file = open('../testData/NexusByAddress.json', "r")
        # json_input = file.read()
        data = json.load(file)
        return data