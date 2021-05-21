pairAPI = {
        'indodax'   : 'https://indodax.com/api/pairs',
        'binance'   : 'https://api.binance.cc/api/v1/ticker/allPrices',
        'bhex'      : 'https://api.bhex.com/openapi/v1/pairs',
        'bitfinex'  : 'https://api.bitfinex.com/v1/symbols',
        'rekeningku': 'https://api.rekeningku.com/v2/coins',
        'luno'      : 'https://api.luno.com/api/1/tickers',
        'gate'      : 'https://data.gateapi.io/api2/1/pairs',
        'bitmart'   : 'https://api-cloud.bitmart.com/spot/v1/symbols',
        'okex'      : 'https://www.okex.com/api/spot/v3/instruments'
    }

tickerAPI = {
        'indodax'   : 'https://indodax.com/api/ticker/',
        'binance'   : 'https://api.binance.cc/api/v3/ticker/price?symbol=',
        'bhex'      : 'https://api.bhex.com/openapi/quote/v1/ticker/price?symbol=',
        'bitfinex'  : 'https://api.bitfinex.com/v1/pubticker/',
        'rekeningku': 'https://api.rekeningku.com/v2/price/', #2
        'luno'      : 'https://api.luno.com/api/1/ticker?pair=',
        'gate'      : 'https://data.gateapi.io/api2/1/ticker/',
        'bitmart'   : 'https://api-cloud.bitmart.com/spot/v1/ticker?symbol=',
        'okex'      : 'https://www.okex.com/api/spot/v3/instruments/' #BTC-USDT/ticker
    }

baseCurrency = {
        'indodax'   : 'IDR',
        'binance'   : 'USDT',
        'bhex'      : 'USDT',
        'bitfinex'  : 'USD',
        'rekeningku': 'IDR',
        'luno'      : 'IDR',
        'gate'      : 'USDT',
        'bitmart'   : 'USDT',
        'okex'      : 'USDT'
    }

priceKey = {
        'indodax'   : 'buy',
        'binance'   : 'price',
        'bhex'      : 'price',
        'bitfinex'  : 'bid',
        'rekeningku': 'c',
        'luno'      : 'bid',
        'gate'      : 'last',
        'bitmart'   : 'last_price',
        'okex'       : 'bid'
    }

isLower = {
        'indodax'   : True,
        'binance'   : False,
        'bhex'      : False,
        'bitfinex'  : True,
        'rekeningku': False,
        'luno'      : False,
        'gate'      : False,
        'bitmart'   : False,
        'okex'      : False
    }

indodax = [
    'XLM','BTT','DGB','NEO','HIVE','ALGO','XMR','CELO','EOS','DASH','ACT','BGT','VSYS','BTS',
    'TRX','ATOM','NXT','COAL','SUMO','FIRO','HNST','ETC','IGNIS','VEX','GXC','HBAR'
    ]

binance = [
    'XLM','ACM','NBS','BTT','DGB','NEO','HIVE','ALGO','XMR','CELO','EOS','DASH','ICX', 'WAVES','NANO',
    'DOCK','BTS','ONG','MBL','SUN','BEAM','RVN','IRIS','WAN','QTUM','XVS','BAKE','WIN','KMD','CTK','RUNE'
    ]

bitfinex = [
    'ADD','ATOM','AVAX','BTSE','CTK','DAPP','DOGE','DOT','EGLD','FIL','JST','LUNA','MOB','NEO','NUT',
    'SOL','XDC','XLM','CLO','XMR','DGB','TRX','QTUM','BTT','LTC','ADA'
    ]

rekeningku = [
    'XLM','NEO','ALGO','TRX','AK12','MIRA'
]

rekeningkuTrade = {
    'XLM':'15','NEO':'25','ALGO':'29','TRX':'24','AK12':'26','MIRA':'47'
}

pair = [
    'XLM', 'BTT', 'HBAR', 'XMR', 'HIVE'
]

suspendList = []
#exchanges       = ['indodax','binance','bhex','bitfinex','gate','bitmart','okex','rekeningku']
exchanges       = ['indodax','binance','bhex','bitfinex','gate','bitmart','okex',]
#exchanges       = ['gate']
pairFrom        = []
exchangeBuy     = 'indodax'
profitTracehold = 1

isFiltered      = False
isDebug         = True
isTimeOut       = False
timeout         = 1 #seconds
