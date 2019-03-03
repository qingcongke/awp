from core.Base import Base
class Simple(Base):


    def __init__(self):
        self.__filename = "config/simple.ini"

        super(Simple,self).__init__(self.__filename)

    
    def run(self):
        huobi = self._createExchange("huobipro")
        print(self.free_balance)
    

