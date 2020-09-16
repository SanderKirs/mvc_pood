import helpers

class Model:
    def __init__(self, items):
        self.items = items

    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)
