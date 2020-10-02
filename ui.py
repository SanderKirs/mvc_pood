# ui.py

# import classes and files
from product import Product
from shop import Shop
from stock import Stock
from controller import Controller
from controller import Stockcontroller
from model import Model
from model import Stockmodel
from view import View
from view import Stockview



# create products
bread = Product("bread", 0.80, 10)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 5)

# create shop and add products to shop
shop = Controller(Model(Shop()), View())
shop.addItem("bread", 0.80, 10)
shop.addItem("wine", 5.60, 5)



# create a stock and add products to the stock

stock = Stockcontroller(Stockmodel(Stock()), Stockview())

stock.addItemStock("apple", 0.80, 10)
stock.addItemStock("melon", 0.9, 75)
stock.addItemStock("bread", 0.80, 90)

shop.addFromStock("bread", 0.50, 90)

# ---Show all items---
shop.showItems()
stock.showItemsStock()



