
#-------Shop-------#

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Item added!")
        except:
            print("Item NOT added!")

    def showItems(self):
        items = self.model.showItems()
        self.view.showItems(items)

    def showItem(self, name):
        try:
            item = self.model.showItem(name)
            self.view.showItem(item)
        except:
            self.view.noItemError(name)

    def deleteItem(self, name):
        try:
            self.model.deleteItem(name)
            self.view.deleteItem(name)
        except:
            self.view.noItemError(name)

    def deleteAllItems(self):
        try:
            self.model.deleteAllItems()
            self.view.deleteAllItems()
        except:
            self.view.ListEmpty()

    def updateItem(self,name, price, amount):
        try:
            self.model.updateItem(name, price, amount)
            self.view.updateItem(name, price, amount)
        except:
            self.view.noItemError(name)

    def addFromStock(self, name, price, takeAmount):
        try:
            self.model.addFromStock(name, price, takeAmount)
            self.view.addFromStock(name, price, takeAmount)
        except:
            self.view.noItemError(name)



#-------Stock-------#

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
            self.stockview.noItemErrorStock(name)

    def addFromStock(self, name, price, takeAmount):
        try:
            self.model.addFromStock(name, price, takeAmount)
            self.view.addFromStock(name, price, takeAmount)
        except:
            self.view.noItemError(name)