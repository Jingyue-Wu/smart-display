import requests
from requests import Session
import constants
import pprint
import serial
import time

# Plug in arduino into serial before running file
ser = serial.Serial(constants.USB_SERIAL_PORT, 9600)

def write(data):
    ser.write(data.encode())

#Write Codes
clear = "/"
green = "{"
red = "}"
row1 = "["
row2 = "]"

parameters ={
    "symbol": "BTC,ETH",
    "convert": "USD"
}
# "symbol": "BTC,ETH,ADA,SOL,DOT,ALGO",

# https://coinmarketcap.com/api/documentation/v1

class CMC:
    def __init__(self, key):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getPrice(self, parameters):
        url = self.apiurl + "/v1/cryptocurrency/quotes/latest"
        request = self.session.get(url, params=parameters)

        for i in parameters["symbol"]:
            pass

        data = request.json()["data"]["BTC"]["quote"]["USD"]["price"]
        return data
    
def sendData(dataList):

    # dataList: [[symbol, price, changePercent], [symbol, price, changePercent], ...]

    for i in dataList:
        write(row1)
        write(f"{dataList[i][0]}: ${dataList[i][1]}")
        write(row2)
        write(f"{dataList[i][0]}: {dataList[i][1]}")



def main():
    cmc = CMC(constants.API_KEY)
    pprint.pprint(cmc.getPrice(parameters))

  

main()