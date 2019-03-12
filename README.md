## CoinSpy


CoinSpy uses current information on https://coinmarketcap.com/ and calculates the changes of the value of different coins in %.
Every 5 minutes an update is made and saved in a txt file for each coin.

For example:
Bitcoin:  
$4202.47 %-Value: 100.0 12/09/2017 19:40:28  
$4097.38 %-Value: 97.5 12/09/2017 20:44:24  
$4093.83 %-Value: 97.41 12/09/2017 21:01:22  
$4094.13 %-Value: 97.42 12/09/2017 21:06:26  

Currently 6 coins are used. ( Bitcoin, Litecoin, Bytecoin, ReddCoin, Vertcoin and Dogecoin ).
You can add any coin you want. Just use the case sensitive name from https://coinmarketcap.com/ and add it in the main.py after or instead of the current coins.
A coinspecific txt file is created automatically.

Setting your own starting limit is easy too. Just delete everything in the current coinspy.txt file and add your own starting value:
$4202.47 %-Value: 100.0
After starting the programm, all values are calculated based on the set value.

For example: insert the value at which you bought the coin. Now you can track at what percentage the coin changed based on his starting value.

## What you need

 python 2.7 with some dependencies 
 (pandas, enum34, numpy, lxml, html5lib ,beautifulsoup4)

## Usage
python main.py
Every 5 minutes an update is made automatically and saved to the txt file.
(if you have python 2 and python3 installed use py -2 main.py )

## Donate
Bitcoin: 17C7sAiGw7a7g7wZx3eVbe5Vuqs35EJhSL    
Litecoin: LLCmNPWBt8TxnNuaTWfyDdajXM5rZPuzsT  
Verge : DN5QsxVaFLykVykGNFqRdGFvi5zg2zz3Rq   
Reddcoin: Rsjofwt2TNu6Gf6eQdzyUhJe2J6vLsKoBq  
Dogecoin: DM13fiivexaZf35HTQ7AKBFLxNTHhJXu1c  
Vertcoin: VbKfmr7B352WEPs3Qi7VeC4WviGS1jGQvd  


## License

MIT License

Copyright (c) 2017 Mastercorp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


