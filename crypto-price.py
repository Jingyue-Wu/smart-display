import requests
from requests import Session
import constants
import serial
import time
import datetime

# Plug in arduino into serial before running file
ser = serial.Serial(constants.USB_SERIAL_PORT, 9600)

def write(data):
    ser.write(data.encode())

clear = "/"
green = "{"
red = "}"
row1 = "["
row2 = "]"

# ----------------------------Options:----------------------------
# Search for any coin
parameters = {"symbol": "BTC,ETH,ADA,SOL,DOT,ALGO", "convert": "USD"}

# Display Weather and time?
displayWeatherTime = True

# LED on?
ledOn = True


def getWeather(key):
    apiurl = "http://api.weatherapi.com/v1"
    location = constants.WETHER_LOCATION
    url = f"{apiurl}/current.json?key={key}&q={location}&aqi=no"
    response = requests.get(url).json()

    tempC = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]
    weather = f"{int(tempC)}C {condition}"

    humidity = response["current"]["humidity"]
    humidString = f"Humidity: {humidity}%"

    return([location, weather, humidString])
     


def displayTimeWeather():
    weatherData = getWeather(constants.WEATHER_API_KEY)

    list = [weatherData[0]]
    hour = "%02d" % datetime.datetime.now().hour
    min = "%02d" % datetime.datetime.now().minute

    time = f"{hour}:{min}"

    # Display Date instead of humidity
    # DD/MM/YYYY format
    # day = "%02d" % datetime.date.today().day
    # month = "%02d" % datetime.date.today().month
    # date = f"{day}-{month}-{datetime.date.today().year}"

    r1 = f"{time}"
    list.append(r1)

    r2 = weatherData[1]
    list.append(r2)

    r3 = weatherData[2]
    list.append(r3)
    return list


class CMC:
    def __init__(self, key):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getPrice(self, parameters):
        url = self.apiurl + "/v1/cryptocurrency/quotes/latest"
        request = self.session.get(url, params=parameters)

        def getData(coin):
            data = [
                coin,
                ("%.2f" %
                 request.json()["data"][coin]["quote"]["USD"]["price"]),
                ("%.2f" % request.json()["data"][coin]["quote"]["USD"]
                 ["percent_change_1h"]),
                ("%.2f" % request.json()["data"][coin]["quote"]["USD"]
                 ["percent_change_7d"])
            ]
            return data

        coinList = parameters["symbol"].split(",")
        list = []
        if displayWeatherTime == True:
            list.append(displayTimeWeather())

        for i in coinList:
            list.append(getData(i))
        return list


def sendData(dataList):
    # dataList format: [[symbol, price, percentChange1h, percentChange7d], ...]

    for i in range(len(dataList)):
        if i == len(dataList):
            i = 0

        if((len(dataList[i][0]) < 5)):

            if ledOn:
                if float(dataList[i][2]) > 0:
                    write(green)
                else:
                    write(red)

            write(clear)
            time.sleep(.1)
            write(row1)
            write(f"{dataList[i][0]}: ${dataList[i][1]}")

            write(row2)
            write(f"Hour: {dataList[i][2]}%")

            time.sleep(2)
            write(row2)
            write("")
            time.sleep(3)
            write(f"Week: {dataList[i][3]}%")

        else: 
            write(green)
            write(clear)
            time.sleep(.1)
            write(row1)
            write(f"{dataList[i][0]}  {dataList[i][1]}")

            write(row2)
            write(f"{dataList[i][2]}")

            time.sleep(3)
            write(row2)
            write("")
            time.sleep(4)
            write(f"{dataList[i][3]}")

        time.sleep(2)


def main():
    cmc = CMC(constants.CMC_API_KEY)
    print("Running!")
    while True:
        sendData(cmc.getPrice(parameters))
        time.sleep(2)


main()