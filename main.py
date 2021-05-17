import requests
import time

indodaxGetPairs = 'https://indodax.com/api/pairs'
binanceGetPairs = 'https://api.binance.cc/api/v1/ticker/allPrices'
bhexGetPairs    = 'https://api.bhex.com/openapi/v1/pairs'
bitfinexGetPairs= 'https://api.bitfinex.com/v1/symbols'

indodaxTicker   = 'https://indodax.com/api/ticker/'
binanceTicker   = 'https://api.binance.cc/api/v3/ticker/price?symbol='
bhexTicker      = 'https://api.bhex.com/openapi/quote/v1/ticker/price?symbol='
bitfinexTicker  = 'https://api.bitfinex.com/v1/pubticker/'

indodaxMain = 'IDR'
binanceMain = 'USDT'
bhexMain    = 'USDT'
bitfinexMain= 'USD'

fromIndodax = [
    'XLM','BTT','DGB','NEO','HIVE','ALGO','XMR','CELO','EOS','DASH',
    'BCH','ACT','BGT','VSYS','BTS','TRX','ATOM','NXT','COAL',
    'SUMO','FIRO','HNST','BCHA','ETC','PAXG','IGNIS'
    ]
fromBinance = [
    'XLM','ACM','NBS','BTT','DGB','NEO','HIVE','ALGO','XMR','CELO','EOS','DASH','ICX',
    'WAVES','NANO','DOCK','BTS','ONG','MBL','SUN','BEAM','RVN','IRIS','WAN',
    'QTUM','XVS','BAKE','WIN','KMD','CTK','RUNE'
    ]

arbitFrom = 'binance'

def main():
    if arbitFrom == 'binance':
        #Arbit from Binance to Indodax Exchange
        print('\nTOKEN\t BINANACE\tIDX\t\tPERCENTAGE')
        idxUSDT = float(requests.get(indodaxTicker+'usdtidr').json()['ticker']['sell'])
        indodaxPair = getIndodaxPair()
        for i in fromBinance:
            try:
                if (i+indodaxMain) in indodaxPair:
                    toPrice = float(requests.get(indodaxTicker+(i+indodaxMain).lower()).json()['ticker']['sell'])/idxUSDT
                    fromPrice = float(requests.get(binanceTicker+i+binanceMain).json()['price'])
                    percentage = (toPrice - fromPrice) / fromPrice * 100
                    #if percentage > 1:
                    print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
            except requests.exceptions.Timeout:
                # Maybe set up for a retry, or continue in a retry loop
                print('Timeout.....')
            except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                print('Too many redirect....')
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

        #Arbit from Binance to BHEX Exchange
        print('\nTOKEN\t BINANACE\tBHEX\t\tPERCENTAGE')
        bhexPair = getBhexPair()
        for i in fromBinance:
            try:
                if (i+bhexMain) in bhexPair:
                    toPrice = float(requests.get(bhexTicker+i+bhexMain).json()['price'])
                    fromPrice = float(requests.get(binanceTicker+i+binanceMain).json()['price'])
                    percentage = (toPrice - fromPrice) / fromPrice * 100
                    #if percentage > 1:
                    print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
            except requests.exceptions.Timeout:
                # Maybe set up for a retry, or continue in a retry loop
                print('Timeout.....')
            except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                print('Too many redirect....')
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

        #Arbit from Binance to Bitfinex Exchange
        print('\nTOKEN\t BINANACE\tBITFINEX\tPERCENTAGE')
        bitfinexPair = getBitfinexPair()
        for i in fromBinance:
            try:
                if ((i+bitfinexMain).lower()) in bitfinexPair:
                    toPrice = float(requests.get(bitfinexTicker+(i+bitfinexMain).lower()).json()['last_price'])
                    fromPrice = float(requests.get(binanceTicker+i+binanceMain).json()['price'])
                    percentage = (toPrice - fromPrice) / fromPrice * 100
                    #if percentage > 1:
                    print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
            except requests.exceptions.Timeout:
                # Maybe set up for a retry, or continue in a retry loop
                print('Timeout.....')
            except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                print('Too many redirect....')
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

    elif arbitFrom == 'indodax':
        #Arbit from Indodax to Binance Exchange
        print('\nTOKEN\t IDX\t\t BINANACE\tPERCENTAGE')
        idxUSDT = float(requests.get(indodaxTicker+'usdtidr').json()['ticker']['sell'])
        binancePair = getBinancePair()
        for i in fromIndodax:
            try:
                if (i+binanceMain) in binancePair:
                    toPrice = float(requests.get(binanceTicker+i+binanceMain).json()['price'])
                    fromPrice = float(requests.get(indodaxTicker+(i+indodaxMain).lower()).json()['ticker']['sell'])/idxUSDT
                    percentage = (toPrice - fromPrice) / fromPrice * 100
                    #if percentage > 1:
                        #print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
                    print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
            except requests.exceptions.Timeout:
                # Maybe set up for a retry, or continue in a retry loop
                print('Timeout.....')
            except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                print('Too many redirect....')
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

        #Arbit from Indodax to BHEX Exchange
        print('\nTOKEN\t IDX\t\t BHEX\t\tPERCENTAGE')
        idxUSDT = float(requests.get(indodaxTicker+'usdtidr').json()['ticker']['sell'])
        bhexPair = getBhexPair()
        for i in fromIndodax:
            try:
                if (i+bhexMain) in bhexPair:
                    toPrice = float(requests.get(bhexTicker+i+bhexMain).json()['price'])
                    fromPrice = float(requests.get(indodaxTicker+(i+indodaxMain).lower()).json()['ticker']['sell'])/idxUSDT
                    percentage = (toPrice - fromPrice) / fromPrice * 100
                    #if percentage > 1:
                        #print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
                    print(i.upper(),'\t',"$%.5f"%fromPrice,'\t$%.5f'%toPrice,'\t%.2f'%percentage,'%')
            except requests.exceptions.Timeout:
                # Maybe set up for a retry, or continue in a retry loop
                print('Timeout.....')
            except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                print('Too many redirect....')
            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                raise SystemExit(e)

def getIndodaxPair():
    res = requests.get(indodaxGetPairs).json()
    indodaxPair = []
    for i in res:
        if i['symbol'].find('IDR') != -1:
            indodaxPair.append(i['symbol'])
    return indodaxPair

def getBinancePair():
    res = requests.get(binanceGetPairs).json()
    binancePair = []
    for i in res:
        if i['symbol'].find(binanceMain) != -1:
            binancePair.append(i['symbol'])
    return binancePair

def getBhexPair():
    res = requests.get(bhexGetPairs).json()
    bhexPair = []
    for i in res:
        if i['symbol'].find(bhexMain) != -1:
            bhexPair.append(i['symbol'])
    return bhexPair

def getBitfinexPair():
    res = requests.get(bitfinexGetPairs).json()
    bitfinexPair = []
    for i in res:
        if i.find(bitfinexMain.lower()) != -1 and i.find(':') == -1:
            bitfinexPair.append(i)
    return bitfinexPair



'''
getPairList()  
'''


while 1==1:
    try:     
        main()
        print("=====================================================\n\n")
        time.sleep(10)
    except KeyboardInterrupt:
        print('Closed.....')
        break

