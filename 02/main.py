import studentcard as sc
from mainshopchanger import MainShopChanger as msc

if __name__ == '__main__':
    studentCard1 = sc.StudentCard(0, "tut", "豊橋/科学/技術/大学", "./imgs/tut.jpg")
    studentCard2 = sc.StudentCard(1, "tenpaku", "天伯町公式アカウント(偽)です。", "./imgs/tenpaku.png")

    studentCard1.setMoney(200)

    msc.insertStudentCard(0)

    msc.chargeMoney(1000)
    msc.dischargeMoney(300)

    msc.insertStudentCard(1)
    msc.chargeMoney(500)
    msc.dischargeMoney(1000)
