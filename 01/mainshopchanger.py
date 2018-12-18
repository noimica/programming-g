import studentcard as sc

class MainShopChanger:
    insertedStudentCard = None
    
    @classmethod
    def insertStudentCard(self, _number):
        MainShopChanger.insertedStudentCard = sc.StudentCard.cardlist(_number)
    
    @classmethod
    def chargeMoney(self, _money):
        if MainShopChanger.insertedStudentCard is None:
            print("学生証が挿入されていません")
            return
        MainShopChanger.insertedStudentCard.chargeMoney(_money)
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

