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