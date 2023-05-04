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
    "symbol": "BTC,ETH,ADA,SOL,DOT,ALGO",
    "convert": "USD"
}

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

        list = []
        btc = ["BTC", ("%.2f" % request.json()["data"]["BTC"]["quote"]["USD"]["price"]), ("%.2f" % request.json()["data"]["BTC"]["quote"]["USD"]["percent_change_1h"]), ("%.2f" % request.json()["data"]["BTC"]["quote"]["USD"]["percent_change_7d"])]
        list.append(btc)
        eth = ["ETH", ("%.2f" % request.json()["data"]["ETH"]["quote"]["USD"]["price"]), ("%.2f" % request.json()["data"]["ETH"]["quote"]["USD"]["percent_change_1h"]), ("%.2f" % request.json()["data"]["ETH"]["quote"]["USD"]["percent_change_7d"])]
        list.append(eth)
        ada = ["ADA", ("%.2f" % request.json()["data"]["ADA"]["quote"]["USD"]["price"]), ("%.2f" % request.json()["data"]["ADA"]["quote"]["USD"]["percent_change_1h"]), ("%.2f" % request.json()["data"]["ADA"]["quote"]["USD"]["percent_change_7d"])]
        list.append(ada)
        sol = ["SOL", ("%.2f" % request.json()["data"]["SOL"]["quote"]["USD"]["price"]), ("%.2f" % request.json()["data"]["SOL"]["quote"]["USD"]["percent_change_1h"]), ("%.2f" % request.json()["data"]["SOL"]["quote"]["USD"]["percent_change_7d"])]
        list.append(sol)
        dot = ["DOT", ("%.2f" % request.json()["data"]["DOT"]["quote"]["USD"]["price"]), ("%.2f" % request.json()["data"]["DOT"]["quote"]["USD"]["percent_change_1h"]), ("%.2f" % request.json()["data"]["DOT"]["quote"]["USD"]["percent_change_7d"])]
        list.append(dot)
        algo = ["ALGO", ("%.2f" % request.json()["data"]["ALGO"]["quote"]["USD"]["price"]), ("%.2f" % request.json()["data"]["ALGO"]["quote"]["USD"]["percent_change_1h"]), ("%.2f" % request.json()["data"]["ALGO"]["quote"]["USD"]["percent_change_7d"])]
        list.append(algo)
        return list
    
def sendData(dataList):

    # dataList format: [[symbol, price, percentChange1h, percentChange7d], [symbol, price, percentChange1h, percentChange7d], ...]

    for i in range(len(dataList)):
        if i == len(dataList):
            i = 0
        if float(dataList[i][3]) > 0:
            write(green)
        else:
            write(red)
        print(i)
        write(clear)
        time.sleep(.1)
        write(row1)
        write(f"{dataList[i][0]}: ${dataList[i][1]}")
        
        write(row2)
        write(f"Hour: {dataList[i][2]}%")

        time.sleep(0.5) 
        write(row2)
        write("")
        time.sleep(3)   
        write(f"Week: {dataList[i][3]}%")


        time.sleep(2)
    

def main():
    cmc = CMC(constants.API_KEY)
    while True:
        pprint.pprint(cmc.getPrice(parameters))
        sendData(cmc.getPrice(parameters))
        time.sleep(2)
main()