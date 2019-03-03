import ccxt

# from variable id
exchange_id = 'huobipro'

try:

    exchange_class = getattr(ccxt, exchange_id)
    exchange = exchange_class({
        'apiKey': 'cc9a5675-df357944-71c7f6c0-c1e35',
        'secret': 'ddab9873-f3a893c0-1f2f79de-8c13c',
        'timeout': 30000,
        'enableRateLimit': True,
    })
    exchange.load_markets()
    print(exchange.id)
    for 
#
#    if symbol not in exchange.markets:
#        raise Exception(exchange.id + ' does not have symbol ' + symbol)
#
#    if not exchange.has['fetchOHLCV']:
#        raise Exception(
#            exchange.id + ' does not support the fetchOHLCV method')
#
#    ohlcv = exchange.markets
#    print(ohcv)
except Exception as e:
    print(type(e).__name__, e.args)
