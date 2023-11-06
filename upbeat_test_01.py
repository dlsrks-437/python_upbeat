import requests

import time

import pprint
import json

while True:
    url = 'https://api.upbit.com/v1/ticker'

    param = {"markets" : "KRW-BTC"}

    response = requests.get(url, params = param)

    # print(response.text)

    result = response.json()
    print(result[0]["trade_price"])

    time.sleep(2)




