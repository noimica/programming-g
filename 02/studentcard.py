from PIL import Image
import gensim

model = gensim.models.Word2Vec.load('./wikimodel/word2vec.gensim.model')


class StudentCard:
    _cardlist = {}

    def __init__(self, _number, _name, _freetext, _img_pass):
        # IDを文字列で管理
        self.setNumber(_number)
        self.setName(_name)
        self.setMoney(0)
        self.interesting = list()
        self.setFreeText(_freetext)
        self.setImg(_img_pass)

    def getNumber(self):
        return int(self.number)

    def setNumber(self, _number):
        self.number = str(_number).zfill(6)
        StudentCard._cardlist[self.number] = self

    def getName(self):
        return self.name

    def setName(self, _name):
        self.name = _name

    def getMoney(self):
        return self.money

    def setMoney(self, _money):
        self.money = _money

    def chargeMoney(self, _money):
        self.money += _money

    def dischargeMoney(self, _money):
        if self.money < _money:
            return False
        self.money -= _money
        return True

    def setImg(self, _img_pass):
        try:
            self.img = Image.open(_img_pass)
        except:
            self.img = None

    def showImg(self):
        if self.img is not None:
            self.img.show()

    def getFreeText(self):
        return self.freetext

    def setFreeText(self, _freetext):
        self.freetext = _freetext
        if "/" in self.freetext:
            pos = self.freetext.split('/')
            results = model.most_similar(positive=pos)
            for result in results:
                self.interesting.append(result[0])

    def getInteresting(self):
        return self.interesting

    @classmethod
    def cardlist(self, _number):
        return self._cardlist[str(_number).zfill(6)]
