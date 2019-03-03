import ccxt
from configparser import ConfigParser
from core.Data import Data


class Base:


    def __init__(self,filename):
        self.__initConfig(filename)

    def __initConfig(self):
        self.__config = ConfigParser()
        self.__config.read(filename,encoding='UTF-8')

    def _getConfigKey(self,group,key):
        return self.__config[group][key]

    def _getConfigGroup(self,group):
        return self.__config[group]


    def _createExchange(self,exchange):
        __exchange_class =  getattr(ccxt,exchange)
        self.__exchange = __exchange_class({
            'apiKey': self._getConfigKey(exchange,"apiKey"),
            'secret': self._getConfigKey(exchange,"secret"),
            'timeout': 30000,
            'enableRateLimit': True,
        })
        self.__exchange.load_markets()
        return self.__exchange

    @property
    def free_balance(self):
        balance =self.__exchange.fetch_free_balance()
        # surprisingly there are balances with 0, so we need to filter these out
        return {k: v for k, v in balance.items() if v > 0}
