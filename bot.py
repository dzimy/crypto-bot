from pybit.unified_trading import HTTP
import os, time

api_key = os.getenv("BYBIT_KEY")
api_secret = os.getenv("BYBIT_SECRET")

def trade():
    session = HTTP(api_key, api_secret)
    while True:
        ticker = session.get_tickers(symbol="PEPEUSDT")
        print(f"Price: {ticker['result']['list'][0]['last_price']}")
        time.sleep(60)

if __name__ == "__main__":
    trade()
