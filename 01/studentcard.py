class StudentCard:
    _cardlist = {}
    
    def __init__(self, _number, _name):
        #IDを文字列で管理
        self.number = str(_number).zfill(6)
        self.name = _name
        self.money = 0
        StudentCard._cardlist[self.number] = self
    
    def getNumber(self):
        return self.number
    def setNumber(self, _number):
        self.number = _number
    
    def getName(self):
        return self.name
    def setName(self, _name):
        self.number = _name
    
    def getMoney(self):
        return self.money
    def setMoney(self, _money):
        self.money = _money
    def chargeMoney(self, _money):
        self.money += _money
    def dischargeMoney(self, _money):
        if self.money < _money :
            return False
        self.money -= _money
        return True
    
    @classmethod
    def cardlist(self, _number):
        return self._cardlist[str(_number).zfill(6)]

