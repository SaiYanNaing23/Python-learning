class ResturantTable :
    menu = {
        "pizza" : 5000,
        "cola" : 600,
        "apple juice" : 2000,
        "hamburger" : 1000,
        "fried potato" : 1500,
    }

    def __init__(self) -> None:
        self.total = 0
        self.orders = []
    
    def addOrder(self,order):
        self.orders.append(order)
        self.total += self.menu[order]

    def printBill(self):
        for order in self.orders:
            print(f"{order} : {self.menu[order]}")

        print(f"Your total bills is {self.total}")

def startProgram() :
    table = ResturantTable()

    while True:
        order = input("Order : ")
        table.addOrder(order)

        another = input("Order again y or n ? :")
        if another == "y":
            continue
        elif another == "n":
            table.printBill()
            break

startProgram()
