import helpers

#-------Shop-------#

class Model:

    def __init__(self, items):
        self.items = items

    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)

    def showItems(self):
        return helpers.showItems()

    def showItem(self, name):
        return helpers.showItem(name)

    def deleteItem(self, name):
        return helpers.deleteItem(name)

    def deleteAllItems(self):
        return helpers.deleteAllItems()

    def updateItem(self,name, price, amount):
        helpers.updateItem(name, price, amount)

    def addFromStock(self, name, price, newAmount):
        helpers.addFromStock(name, price, newAmount)

#-------Stock-------#

class Stockmodel:

    def __init__(self, stockItems):
        self.items = stockItems

    def addItemStock(self, name, price, amount):
        helpers.addItemStock(name, price, amount)

    def showItemsStock(self):
        return helpers.showItemsStock()

    def showItemStock(self, name):
        return helpers.showItemStock(name)

    def deleteItemStock(self, name):
        return helpers.deleteItemStock(name)

    def deleteAllItemsStock(self):
        return helpers.deleteAllItemsStock()

    def updateItemStock(self,name, price, amount):
        return helpers.updateItemStock(name, price, amount)