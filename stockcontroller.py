

class Stockcontroller:
    def __init__(self, stockmodel, stockview):
        self.stockmodel = stockmodel
        self.stockview = stockview

    def addItemStock(self, name, price, amount):
        try:
            self.stockmodel.addItemStock(name, price, amount)
            print("Ok!")
        except:
            print("Problem!")

    def showItemsStock(self):
        stockItems = self.stockmodel.showItemsStock()
        self.stockview.showItemsStock(stockItems)

    def showItemStock(self, name):
        try:
            stockItems = self.stockmodel.showItemStock(name)
            self.stockview.showItemStock(stockItems)
        except:
            self.stockview.noItemError(name)

    def deleteItemStock(self, name):
        try:
            self.stockmodel.deleteItemStock(name)
            self.stockview.deleteItemStock(name)
        except:
            self.stockview.noItemError(name)

    def deleteAllItemsStock(self):
        try:
            self.stockmodel.deleteAllItemsStock()
            self.stockview.deleteAllItemsStock()
        except:
            self.stockview.ListEmpty()

    def updateItemStock(self,name, price, amount):
        try:
            self.stockmodel.updateItemStock(name, price, amount)
            self.stockview.updateItemStock(name, price, amount)
        except:
            self.stockview.noItemError(name)