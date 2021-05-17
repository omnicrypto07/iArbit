import requests
import time
import re
import config

pairAPI = {
        'indodax'   : 'https://indodax.com/api/pairs',
        'binance'   : 'https://api.binance.cc/api/v1/ticker/allPrices',
        'bhex'      : 'https://api.bhex.com/openapi/v1/pairs',
        'bitfinex'  : 'https://api.bitfinex.com/v1/symbols',
        'rekeningku': 'https://api.rekeningku.com/v2/coins',
        'luno'      : 'https://api.luno.com/api/1/tickers',
        'gate'      : 'https://data.gateapi.io/api2/1/pairs'
    }

tickerAPI = {
        'indodax'   : 'https://indodax.com/api/ticker/',
        'binance'   : 'https://api.binance.cc/api/v3/ticker/price?symbol=',
        'bhex'      : 'https://api.bhex.com/openapi/quote/v1/ticker/price?symbol=',
        'bitfinex'  : 'https://api.bitfinex.com/v1/pubticker/',
        'rekeningku': 'https://api.rekeningku.com/v2/price/',
        'luno'      : 'https://api.luno.com/api/1/ticker?pair=',
        'gate'      : 'https://data.gateapi.io/api2/1/ticker/'
    }

baseCurrency = {
        'indodax'   : 'IDR',
        'binance'   : 'USDT',
        'bhex'      : 'USDT',
        'bitfinex'  : 'USD',
        'rekeningku': 'IDR',
        'luno'      : 'IDR',
        'gate'      : 'USDT'
    }

priceKey = {
        'indodax'   : 'buy',
        'binance'   : 'price',
        'bhex'      : 'price',
        'bitfinex'  : 'bid',
        'rekeningku': 'c',
        'luno'      : 'bid',
        'gate'      : ''
    }

isLower = {
        'indodax'   : True,
        'binance'   : False,
        'bhex'      : False,
        'bitfinex'  : True,
        'rekeningku': False,
        'luno'      : False,
    }

indodax = [
    'XLM','BTT','DGB','NEO','HIVE','ALGO','XMR','CELO','EOS','DASH','BCH','ACT','BGT','VSYS','BTS',
    'TRX','ATOM','NXT','COAL','SUMO','FIRO','HNST','BCHA','ETC','PAXG','IGNIS','VEX','GXC','HBAR'
    ]

binance = [
    'XLM','ACM','NBS','BTT','DGB','NEO','HIVE','ALGO','XMR','CELO','EOS','DASH','ICX', 'WAVES','NANO',
    'DOCK','BTS','ONG','MBL','SUN','BEAM','RVN','IRIS','WAN','QTUM','XVS','BAKE','WIN','KMD','CTK','RUNE'
    ]

bitfinex = [
    'ADD','ATOM','AVAX','BTSE','CTK','DAPP','DOGE','DOT','EGLD','FIL','JST','LUNA','MOB','NEO','NUT',
    'SOL','XDC','XLM','CLO','XMR','DGB','BTG','TRX','QTUM','BTT','LTC','ADA'
    ]

suspendList = ['ALGO', 'EOS']

exchanges       = ['indodax','binance','bhex','bitfinex','rekeningku', 'luno']
#exchanges       = ['indodax', 'luno']
pairFrom        = []
exchangeBuy     = 'indodax'
isFiltered      = False
indodaxUSDT     = float(requests.get(tickerAPI['indodax']+'usdtidr').json()['ticker']['sell'])
rekeningkuUSDT  = float(requests.get(tickerAPI['rekeningku']+'20').json()['c'])
print('USDT','Indodax',indodaxUSDT,', Rekeningku',rekeningkuUSDT)

def getProfitByExchange(exchangeBuy, exchangeSell, tradeList, baseCurrencyBuy, baseCurrencySell):
    #Arbit Calculator
    print("=====================================================")
    print('TOKEN\t %s\t%s\t\t'%(exchangeBuy.upper(),exchangeSell.upper()))
    pairList = getPairList(exchangeSell, tradeList)
    
    for i in pairList:
        #Buy Code Checker
        if exchangeBuy == 'rekeningku':
            buyCode = str(parlist[i])
        else:
            buyCode = i+baseCurrencyBuy

        #Sell Code Checker
        if exchangeSell == 'rekeningku':
            sellCode = str(pairList[i])
        else:
            sellCode = i+baseCurrencySell

        #Lowercase API Checker
        if isLower[exchangeBuy]==True:
            buyCode = buyCode.lower()
        if isLower[exchangeSell]==True:
            sellCode = sellCode.lower()

        #Buy Price Checker
        if exchangeBuy == 'indodax':
            buyPrice    = float(requests.get(tickerAPI[exchangeBuy]+buyCode).json()['ticker']['sell'])/indodaxUSDT
        elif exchangeBuy == 'rekeningku':
            buyPrice    = float(requests.get(tickerAPI[exchangeBuy]+buyCode).json()[priceKey[exchangeBuy]])/rekeningkuUSDT
        else:
            try:
                buyPrice = float(requests.get(tickerAPI[exchangeBuy]+buyCode).json()[priceKey[exchangeBuy]])
            except (IndexError, KeyError, TypeError):
                buyPrice = -1000
                #print(buyPrice,IndexError, KeyError, TypeError)
            
            
        #Sell Price Checker
        if exchangeSell == 'indodax':
            sellPrice   = float(requests.get(tickerAPI[exchangeSell]+sellCode).json()['ticker']['buy'])/indodaxUSDT
        elif exchangeSell == 'rekeningku':
            sellPrice   = float(requests.get(tickerAPI[exchangeSell]+sellCode).json()[priceKey[exchangeSell]])/rekeningkuUSDT
        else:
            sellPrice   = float(requests.get(tickerAPI[exchangeSell]+sellCode).json()[priceKey[exchangeSell]])
            
        percentage = (sellPrice - buyPrice) / buyPrice * 100
        #print(exchangeBuy,exchangeSell,buyCode,sellCode,buyPrice,sellPrice)
        if isFiltered:
            if percentage > 1:
                print(i.upper(),'\t',"$%.5f"%buyPrice,'\t$%.5f'%sellPrice,'\t%.2f'%percentage,'%')
        else:
            if buyPrice != -1000:
                print(i.upper(),'\t',"$%.5f"%buyPrice,'\t$%.5f'%sellPrice,'\t%.2f'%percentage,'%')
        #print()
    print("=====================================================\n\n")

def getPairList(exchangeSell, tradeList):
    res = requests.get(pairAPI[exchangeSell]).json()
    pairs = []
    if exchangeSell == 'bitfinex':
        for i in res:
            if i.find(baseCurrency[exchangeSell].lower()) != -1 and i.find(':') == -1:
                code = re.sub(baseCurrency[exchangeSell].lower(),'',i).upper()
                if (code in tradeList and code not in suspendList):
                    pairs.append(code)
                    
    elif exchangeSell == 'rekeningku':
        pairs = {}
        for i in res['result']:
            code = i['accountcode']
            if (code in tradeList and code not in suspendList):
                pairs.update({i['accountcode']: i['id']})

    elif exchangeSell == 'luno':
        for i in res['tickers']:
            if i['pair'].find(baseCurrency[exchangeSell]) != -1:
                code = re.sub(baseCurrency[exchangeSell],'',i['pair']).upper()
                if (code in tradeList and code not in suspendList):
                    pairs.append(code)                  
                
    else:
        for i in res:
            if i['symbol'].find(baseCurrency[exchangeSell]) != -1:
                code = re.sub(baseCurrency[exchangeSell],'',i['symbol']).upper()
                if (code in tradeList and code not in suspendList):
                    pairs.append(code)           
    return pairs
    
def main():
    if exchangeBuy == 'binance':
        tradeList = binance
    elif exchangeBuy == 'indodax':
        tradeList = indodax
    elif exchangeBuy == 'bitfinex':
        tradeList = bitfinex

    for i in exchanges:
        if i!=exchangeBuy:
            getProfitByExchange(exchangeBuy, i, tradeList, baseCurrency[exchangeBuy], baseCurrency[i])
#main()

while 1==1:
    try:     
        main()
        time.sleep(5)
    except KeyboardInterrupt:
        print('Closed.....')
        break

