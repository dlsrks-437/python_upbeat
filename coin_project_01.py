import sys
import time

import requests

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *

form_class = uic.loadUiType("Ui/coin_main.ui")[0]

class CoinViewThread(QThread):  # 시그널 클래스

    # 시그널 함수 정의
    coinDataSent = pyqtSignal(float, float, float, float, float, float, float, float, float)

    def __init__(self):
        super().__init__()
        self.alive = True

    def run(self):
        while self.alive:
            url = 'https://api.upbit.com/v1/ticker'

            param = {"markets": "KRW-BTC"}

            response = requests.get(url, params=param)

            result = response.json()

            trade_price = result[0]["trade_price"]  # 비트코인의 현재 가격
            acc_trade_volume_24h = result[0]["acc_trade_volume_24h"]  # 비트코인의 24시간 누적 거래량
            acc_trade_price_24h = result[0]["acc_trade_price_24h"]  # 비트코인의 24시간 누적 거래대금
            trade_volume = result[0]["trade_volume"]  # 비트코인의 가장 최근 거래량
            high_price = result[0]["high_price"]  # 비트코인의 고가
            low_price = result[0]["low_price"]  # 비트코인의 저가
            prev_closing_price = result[0]["prev_closing_price"]  # 비트코인의 전일 종가(UTC 0시 기준)
            signed_change_rate = result[0]["signed_change_rate"]  # 비트코인의 부호가 있는 변화율

            self.coinDataSent.emit(float(trade_price),
                                   float(acc_trade_volume_24h),
                                   float(acc_trade_price_24h),
                                   float(trade_volume),
                                   float(high_price),
                                   float(low_price),
                                   float(prev_closing_price),
                                   float(signed_change_rate) )

            time.sleep(2)

    def close(self):  # 프로그램 종료 없이 while문을 정지
        self.alive = False


class CoinWindow(QMainWindow, form_class):  # 슬롯 클래스

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Coin Price Overview')
        # self.setWindowIcon(QIcon())
        self.statusBar().showMessage(' ver 0.5 ')

        self.cvt = CoinViewThread()  # 시그널 클래스로 객체 선언
        self.cvt.coinDataSent.connect(self.fillCoinData())
        self.cvt.start()  # 시그널 함수의 스레드 시작

    #  시그얼클래스에서 보내중 코인정보를 ui에 출력해주는 슬롯 함수
    def fillCoinData(self, trade_price, acc_trade_volume_24h, acc_trade_price_24h, trade_volume,
                     high_price, low_price, prev_closing_price, signed_change_rate):
        self.price_coin_label.setText(f"{trade_price:, .0f} 원")  # 현재가
        self.coin_change_label.setText(f"{signed_change_rate:+ .2f}")  # 가격변화율 -> 소수 2자리까지
        self.rate_trade_label.setText(f"{acc_trade_volume_24h:, .4f} ")  # 거래량
        self.rate_price_label.setText (f"{acc_trade_price_24h:, .0f} ") # 거래금액
        self.trade_volum_label.setText(f"{trade_volume:, .0f} 원")
        self.price_high_label.setText(f"{high_price:, .0f} 원")
        self.price_low_label.setText(f"{low_price:, .0f} 원")
        self.price_end_label.setText(f"{prev_closing_price:, .0f} 원")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CoinWindow()
    win.show()
    sys.exit(app.exec_())



