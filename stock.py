# stock.py
class Stock:
    def __init__(self):
        self.products = []

    def __repr__(self):
        description = ""
        for product in self.products:
            description += repr(product)
            description += "\n=================\n"
        return description

    def addProductStock(self, product):
        self.products.append(product)