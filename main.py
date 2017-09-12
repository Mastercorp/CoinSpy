import pandas as pd
import time
import array
from enum import Enum
import os.path

class Coin(Enum):
    Bitcoin = 0
    Litecoin = 1
    Bytecoin = 2
    ReddCoin = 3
    Vertcoin = 4
    Dogecoin = 5


def load_coin_value(file_name):
    '''file_name  of type String'''
    try:
        with open(file_name + 'spy.txt', 'r') as f:
            file_content = f.readline()
            whitespace = file_content.find(" ")
            file_content = file_content[1:whitespace]
        return file_content
    except EnvironmentError:
        return False


def save_file(file_name, file_content):
    '''file_name and file_content of type String'''
    try:
        with open(file_name + 'spy.txt', 'a') as f:
            f.write(file_content)
        return True
    except EnvironmentError:
        return False


starttime = time.time()
y = 1
startvalue = array.array('d', (0 for i in range(0, len(Coin))))
while True:
    calls_df, = pd.read_html("https://coinmarketcap.com/all/views/all/", index_col=1, header=0)
    for coin in Coin:
        if not os.path.isfile(coin.name + 'spy.txt'):
            with open(coin.name + 'spy.txt', 'w'):
                pass
        if os.stat(coin.name + 'spy.txt').st_size == 0:
            x = calls_df.loc[coin.name]
            now = time.strftime('%d/%m/%Y %H:%M:%S')
            coinvalue = x[3]
            coinvalue = float(coinvalue[1:])
            startvalue[coin.value] = coinvalue
            coinchange = round((coinvalue / startvalue[coin.value]), 4) * 100
            coininfo = "$" + str(coinvalue) + " %-Value: " + str(coinchange) + " " + now
            save_file(coin.name, coininfo)
        else:
            if y == 1:
                startvalue[coin.value] = float(load_coin_value(coin.name))
            x = calls_df.loc[coin.name]
            now = time.strftime('%d/%m/%Y %H:%M:%S')
            coinvalue = x[3]
            coinvalue = float(coinvalue[1:])
            coinchange = round((coinvalue / startvalue[coin.value]), 4) * 100
            coininfo = "\n" + "$" + str(coinvalue) + " %-Value: " + str(coinchange) + " " + now
            save_file(coin.name, coininfo)
    print "tick " + str(y) + "\n"
    y = y + 1
    time.sleep(300.0 - ((time.time() - starttime) % 300.0))




