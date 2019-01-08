import studentcard as sc
import datetime

class MainShopChanger:
    insertedStudentCard = None
    charged_date = datetime.datetime.today()

    @classmethod
    def insertStudentCard(self, _number):
        MainShopChanger.insertedStudentCard = sc.StudentCard.cardlist(_number)

    @classmethod
    def chargeMoney(self, _money):
        if MainShopChanger.insertedStudentCard is None:
            print("学生証が挿入されていません")
            return
        MainShopChanger.insertedStudentCard.chargeMoney(_money)
        MainShopChanger.charged_date = datetime.datetime.today()
        MainShopChanger.printAccountBalance()

    @classmethod
    def dischargeMoney(self, _money):
        if MainShopChanger.insertedStudentCard is None:
            print("学生証が挿入されていません")
            return False
        if not MainShopChanger.insertedStudentCard.dischargeMoney(_money):
            print("残高が足りません")
            return False
        MainShopChanger.printAccountBalance()
        return True

    @classmethod
    def printAccountBalance(self):
        print("残高を表示します")
        print("学生名:" + str(MainShopChanger.insertedStudentCard.getName()))
        print("残高:" + str(MainShopChanger.insertedStudentCard.getMoney()))
        print("自由記述欄:" + str(MainShopChanger.insertedStudentCard.getFreeText()))
        print("関連のあるもの:" + str(MainShopChanger.insertedStudentCard.getInteresting()))
        print("最新チャージ年月日:" + str(MainShopChanger.charged_date))
        MainShopChanger.insertedStudentCard.showImg()

    @classmethod
    def getChargedDate(self):
        return MainShopChanger.charged_date
