import stockhelpers

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