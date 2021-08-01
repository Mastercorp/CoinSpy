import pandas as pd
import locale
import time
from enum import Enum
import os.path


class Coin(Enum):
    BTCBitcoin = 0
    LTCLitecoin = 1
    ETHEthereum = 2
    DOGEDogecoin = 3


def load_coin_value(file_name):
    """
    load the starting value of a coin for a given file_name
    """
    try:
        with open(file_name + 'spy.txt', 'r') as f:
            file_content = f.readline()
            whitespace = file_content.find(" ")
            file_content = file_content[1:whitespace]
        return file_content
    except EnvironmentError:
        return False


def save_file(file_name, file_content):
    """
    save file_content as coinename + spy.txt
    """
    try:
        with open(file_name + 'spy.txt', 'a') as f:
            f.write(file_content)
        return True
    except EnvironmentError:
        return False


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

buy_value = dict()

for coin in Coin:
    try:
        if os.path.getsize(f"{coin.name}spy.txt") != 0:
            buy_value[coin.name] = float(load_coin_value(coin.name))
    except FileNotFoundError:
        continue

while True:
    calls_df = pd.read_html("https://coinmarketcap.com/all/views/all/", index_col=1, header=0)
    now = time.strftime('%d/%m/%Y %H:%M:%S')
    for coin in Coin:
        coin_info = calls_df[2].loc[coin.name]
        coin_price = float(locale.atof(coin_info.Price[1:]))
        buy_value[coin.name] = buy_value.get(coin.name, coin_price)
        coin_change = coin_price / buy_value[coin.name] * 100
        coin_txt = f"${coin_price} %-Value: {coin_change:.2f} {now} \n"
        save_file(coin.name, coin_txt)

    time.sleep(300)
