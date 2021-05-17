

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
        'gate'      : 'last'
    }

isLower = {
        'indodax'   : True,
        'binance'   : False,
        'bhex'      : False,
        'bitfinex'  : True,
        'rekeningku': False,
        'luno'      : False,
        'gate'      : False
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

#exchanges       = ['indodax','binance','bhex','bitfinex','rekeningku', 'luno']
exchanges       = ['indodax', 'gate']
pairFrom        = []
exchangeBuy     = 'indodax'
isFiltered      = False
isDebug         = True
