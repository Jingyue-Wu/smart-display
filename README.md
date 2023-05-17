# Cryptocurrency Ticker and Smart Display

A sleek and informative smart dispaly that shows local weather and real-time market trends for your favourite coins. Can be powered through USB by any device with an Internet connection and runs `python3`. The Python script runs on host device and forwards live data to Arduino (ATmega328) through USB serial. This system operates without the need of a WiFi module. 

Supports all cryptocurrencies on [CoinMarketCap](https://coinmarketcap.com/api/documentation/v1/)

![DSC_1494](https://github.com/Jingyue-Wu/crypto-ticker/assets/75918217/44a73b64-1537-47d7-bf5f-6497da128f96)
![DSC_1473](https://github.com/Jingyue-Wu/crypto-ticker/assets/75918217/fd9af823-76b9-4ad6-8f0e-d0fb51f99b95)

Instructions assume host device is connected to the Internet, running `Git`, `pip`, `python3`.

# Hardware

* ATmega328 microcontroller board with USB or equivalent
* 16x2 LCD
* Wires
* 220 ohm potentiometer
* 220 ohm resistors x2
* Green and red LED

## Wiring Diagram
![circuit](https://github.com/Jingyue-Wu/crypto-ticker/assets/75918217/22158f94-fce2-49ef-844f-1169b90822d4)

## Compact Case
STL files for 3D printing are provided in `hardware` folder. Case was designed for an Arduino Nano and soldering may be required to fit all hardware components inside. 

# Installation

Clone the required files: 
`git clone https://github.com/Jingyue-Wu/crypto-ticker`

Connect to ticker over USB and update and install necessary packages 
```
pip install pyserial
pip install DateTime
```
Install CH340 USB drivers: [CH341SER](http://www.wch-ic.com/downloads/CH341SER_ZIP.html)

Flash microcontroller with `crypto-ticker.ino` using Arduino IDE


# Configure Constants

Obtain your API keys from:
[CoinMarketCap](https://coinmarketcap.com/api/documentation/v1/)
[Weather API](https://www.weatherapi.com/)

Input API keys, USB serial port and your location in `constants.py`


`crypto-price.py` contains customizable options such as currencies:
```
# ----------------------------Options:----------------------------
# Search for any coin
parameters = {"symbol": "BTC,ETH,ADA,SOL,DOT,ALGO", "convert": "USD"}

# Display Weather and time?
displayWeatherTime = True

# LED on?
ledOn = True
```

# Usage

Plug in microcontroller, then run `crypto-price.py`. Device and program should instantly boot up.
