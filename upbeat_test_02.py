import requests

url = 'https://api.upbit.com/v1/ticker'

param = {"markets": "KRW-BTC"}

response = requests.get(url, params=param)

result = response.json()

print(result[0]["trade_price"])   # 비트코인의 현재 가격
print(result[0]["opening_price"])   # 비트코인의 시가
print(result[0]["high_price"])   # 비트코인의 고가
print(result[0]["low_price"])   # 비트코인의 저가
print(result[0]["prev_closing_price"])   # 비트코인의 전일 종가(UTC 0시 기준)
print(result[0]["acc_trade_volume_24h"])   # 비트코인의 24시간 누적 거래량
print(result[0]["acc_trade_price_24h"])   # 비트코인의 24시간 누적 거래대금
print(result[0]["trade_volume"])   # 비트코인의 가장 최근 거래량
print(result[0]["signed_change_rate"])   # 비트코인의 부호가 있는 변화율







