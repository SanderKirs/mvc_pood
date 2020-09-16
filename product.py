#product.py
class Product:
    def __init__(self, name, price, amount):
        self.setName(name)
        self.setPrice(price)
        self.setAmount(amount)

        #Profuct test view
    def __repr__(self):
            return "name: {} \nprice: {} \namount: {}".format(self.getName(), self.getPrice(), self.getAmount())

    #Setters
    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setAmount(self, amount):
        self.__amount = amount

    #Getters
    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getAmount(self):
        return self.__amount