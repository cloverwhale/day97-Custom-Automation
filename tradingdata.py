import requests
import json

URI = 'https://www.twse.com.tw/zh/fund/'
ENDPOINT_ALL = 'T86'


class TradingData:

    def __init__(self, **kwargs):
        self.parameters = {
            'response': 'json',
            'selectType': 'ALLBUT0999'
        }
        if 'date' in kwargs:
            self.parameters['date'] = kwargs['date']

    def daily(self):
        return self.get_data(ENDPOINT_ALL)

    def get_data(self, endpoint):
        uri = URI + endpoint
        response = requests.get(uri, params=self.parameters)
        response_data = json.loads(response.text)
        return response_data
