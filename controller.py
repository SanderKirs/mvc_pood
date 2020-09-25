class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Ok!")
        except:
            print("Problem!")

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