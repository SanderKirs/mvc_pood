#ui.py

from product import Product
from shop import Shop
from controller import Controller
from model import Model
from view import View

#creating products
bread = Product("Bread", 0.80, 10)
milk = Product("Milk", 0.50, 50)
wine = Product("Wine", 5.60, 5)

#Creating the shop and adding the products to it
shop = Controller(Model(Shop()), View())
shop.addItem("Bread", 0.80, 10)
shop.addItem("Milk", 0.50, 50)
shop.addItem("Wine", 5.60, 5)

print(shop)