import helpers

class Model:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items

    # add item to items
    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)

    # show items
    def showItems(self):
        return helpers.showItems()

    # show item
    def showItem(self, name):
        return helpers.showItem(name)

    def deleteItem(self, name):
        return helpers.deleteItem(name)

    def deleteAllItems(self):
        return helpers.deleteAllItems()

    def updateItem(self,name, price, amount):
        return helpers.updateItem(name, price, amount)


class Stockmodel:
    # get shop data - [] of products
    def __init__(self, stockItems):
        self.items = stockItems

    # add item to items
    def addItemStock(self, name, price, amount):
        stockhelpers.addItemStock(name, price, amount)

    # show items
    def showItemsStock(self):
        return stockhelpers.showItemsStock()

    # show item
    def showItemStock(self, name):
        return stockhelpers.showItemStock(name)

    def deleteItemStock(self, name):
        return stockhelpers.deleteItemStock(name)

    def deleteAllItemsStock(self):
        return stockhelpers.deleteAllItemsStock()

    def updateItemStock(self,name, price, amount):
        return stockhelpers.updateItemStock(name, price, amount)