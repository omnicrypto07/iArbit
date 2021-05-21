import requests
import time
import re
import config

indodaxUSDT     = float(requests.get(config.tickerAPI['indodax']+'usdtidr').json()['ticker']['sell'])
rekeningkuUSDT  = float(requests.get(config.tickerAPI['rekeningku']+'20').json()['c'])

print('USDT','Indodax',indodaxUSDT,', Rekeningku',rekeningkuUSDT)

def getProfitByExchange(exchangeBuy, exchangeSell, tradeList, baseCurrencyBuy, baseCurrencySell):
    #Arbit Calculator
    print("=====================================================")
    print('TOKEN\t %s\t%s\t\t'%(exchangeBuy.upper(),exchangeSell.upper()))
    pairList = getPairList(exchangeSell, tradeList)
    
    for i in pairList:
        #Timeout Set
        if config.isTimeOut == True:
            time.sleep(config.timeout)
        
        #Buy Code Checker
        if exchangeBuy == 'rekeningku':
            buyCode = config.rekeningkuTrade[i]
        elif exchangeBuy == 'gate':
            buyCode = i+'_'+baseCurrencyBuy
        elif exchangeBuy == 'okex':
            buyCode = i+'-'+baseCurrencyBuy+'/ticker'
        else:
            buyCode = i+baseCurrencyBuy

        #Sell Code Checker
        if exchangeSell == 'rekeningku':
            sellCode = str(pairList[i])
        elif exchangeSell == 'gate' or exchangeSell == 'bitmart':
            sellCode = i+'_'+baseCurrencySell
        elif exchangeSell == 'okex':
            sellCode = i+'-'+baseCurrencySell+'/ticker'
        else:
            sellCode = i+baseCurrencySell

        #Lowercase API Checker
        if config.isLower[exchangeBuy]==True:
            buyCode = buyCode.lower()
        if config.isLower[exchangeSell]==True:
            sellCode = sellCode.lower()

        #Buy Price Checker
        if exchangeBuy == 'indodax':
            buyPrice    = float(requests.get(config.tickerAPI[exchangeBuy]+buyCode).json()['ticker']['sell'])/indodaxUSDT
        elif exchangeBuy == 'rekeningku':
            buyPrice    = float(requests.get(config.tickerAPI[exchangeBuy]+buyCode).json()[config.priceKey[exchangeBuy]])/rekeningkuUSDT
        elif exchangeBuy == 'bitmart':
            buyPrice    = float(requests.get(config.tickerAPI[exchangeBuy]+buyCode).json()['data']['tickers'][0])
        elif exchangeBuy == 'okex':
            buyPrice    = float(requests.get(config.tickerAPI[exchangeBuy]+buyCode).json()[config.priceKey[exchangeBuy]])
        else:
            try:
                buyPrice = float(requests.get(config.tickerAPI[exchangeBuy]+buyCode).json()[config.priceKey[exchangeBuy]])
            except (IndexError, KeyError, TypeError):
                buyPrice = -1000
                #print(buyPrice,IndexError, KeyError, TypeError)
            
            
        #Sell Price Checker
        if exchangeSell == 'indodax':
            sellPrice   = float(requests.get(config.tickerAPI[exchangeSell]+sellCode).json()['ticker']['buy'])/indodaxUSDT
        elif exchangeSell == 'rekeningku':
            sellPrice   = float(requests.get(config.tickerAPI[exchangeSell]+sellCode).json()[config.priceKey[exchangeSell]])/rekeningkuUSDT
        elif exchangeSell == 'bitmart':
            sellPrice   = float(requests.get(config.tickerAPI[exchangeSell]+sellCode).json()['data']['tickers'][0]['last_price'])
        elif exchangeSell == 'okex':
            sellPrice   = float(requests.get(config.tickerAPI[exchangeSell]+sellCode).json()[config.priceKey[exchangeSell]])
        else:
            sellPrice   = float(requests.get(config.tickerAPI[exchangeSell]+sellCode).json()[config.priceKey[exchangeSell]])
            
        percentage = (sellPrice - buyPrice) / buyPrice * 100
        #print(exchangeBuy,exchangeSell,buyCode,sellCode,buyPrice,sellPrice)
        if config.isFiltered:
            if abs(percentage) > config.profitTracehold:
                print(i.upper(),'\t',"$%.5f"%buyPrice,'\t$%.5f'%sellPrice,'\t%.2f'%percentage,'%')
        else:
            if buyPrice != -1000:
                print(i.upper(),'\t',"$%.5f"%buyPrice,'\t$%.5f'%sellPrice,'\t%.2f'%percentage,'%')
        #print()
    print("=====================================================\n\n")

def getPairList(exchangeSell, tradeList):
    res = requests.get(config.pairAPI[exchangeSell]).json()
    pairs = []
    if exchangeSell == 'bitfinex':
        for i in res:
            if i.find(config.baseCurrency[exchangeSell].lower()) != -1 and i.find(':') == -1:
                code = re.sub(config.baseCurrency[exchangeSell].lower(),'',i).upper()
                if (code in tradeList and code not in config.suspendList):
                    pairs.append(code)
                    
    elif exchangeSell == 'rekeningku':
        pairs = {}
        for i in res['result']:
            code = i['accountcode']
            if (code in tradeList and code not in config.suspendList):
                pairs.update({i['accountcode']: i['id']})
            
    elif exchangeSell == 'luno':
        for i in res['tickers']:
            if i['pair'].find(config.baseCurrency[exchangeSell]) != -1:
                code = re.sub(config.baseCurrency[exchangeSell],'',i['pair']).upper()
                if (code in tradeList and code not in config.suspendList):
                    pairs.append(code)                  
                
    elif exchangeSell == 'gate':
        for i in res:
            if i.find(config.baseCurrency[exchangeSell]) > 0:
                code = re.sub('_'+config.baseCurrency[exchangeSell],'',i).upper()
                if (code in tradeList and code not in config.suspendList):
                    pairs.append(code)

    elif exchangeSell == 'bitmart':
        for i in res['data']['symbols']:
            if i.find(config.baseCurrency[exchangeSell]) > 0:
                code = re.sub('_'+config.baseCurrency[exchangeSell],'',i).upper()
                if (code in tradeList and code not in config.suspendList):
                    pairs.append(code)

    elif exchangeSell == 'okex':
        for i in res:
            if i['instrument_id'].find(config.baseCurrency[exchangeSell]) > 0:
                code = i['base_currency']
                if (code in tradeList and code not in config.suspendList):
                    pairs.append(code)

    else:
        for i in res:
            if i['symbol'].find(config.baseCurrency[exchangeSell]) != -1:
                code = re.sub(config.baseCurrency[exchangeSell],'',i['symbol']).upper()
                if (code in tradeList and code not in config.suspendList):
                    pairs.append(code)           
    return pairs
    
def main():
    tradeList = []
    if config.exchangeBuy == 'binance':
        tradeList = config.binance
    elif config.exchangeBuy == 'indodax':
        tradeList = config.indodax
    elif config.exchangeBuy == 'bitfinex':
        tradeList = config.bitfinex
    elif config.exchangeBuy == 'bhex':
        tradeList = config.bhex
    elif config.exchangeBuy == 'rekeningku':
        tradeList = config.rekeningku

    for i in config.exchanges:
        if i!=config.exchangeBuy:
            getProfitByExchange(config.exchangeBuy, i, tradeList, config.baseCurrency[config.exchangeBuy], config.baseCurrency[i])
#main()

if config.isDebug:
    main()
else:
    while 1==1:
        try:     
            main()
            time.sleep(10)
        except KeyboardInterrupt:
            print('Closed.....')
            break

