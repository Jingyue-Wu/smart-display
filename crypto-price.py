import requests
from requests import Session
import constants

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': constants.API_KEY,
}

parameters ={
    "symbol": "BTC,ETH,ADA,SOL,DOT,ALGO",
    "convert": "USD"
}

request = requests.get(url, headers=headers)


class CMC:

    def __init__(self, key):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

        def  getPrice(self):
            url = self.apiurl + "/v1/cryptocurrency/quotes/latest"
            request = self.session.get(url, params=parameters)
            data = request.json()["data"]
            return data

def main():
    cmc = CMC(constants.API_KEY)


main()