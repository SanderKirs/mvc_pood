#ui.py

from product import Product
from shop import Shop

#creating products
bread = Product("Bread", 0.80, 10)
milk = Product("Milk", 0.50, 50)
wine = Product("Wine", 5.60, 5)

#Creating the shop and adding the products to it
shop = Shop()
shop.addProduct(bread)
shop.addProduct(milk)
shop.addProduct(wine)

print(shop)