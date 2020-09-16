import exception


#Represents shops structure
#List of Product type objects
items = []

#Add item to items
def addItem(name, price, amount):
    #Create the product with the required descriptions
    product = Product("name, price, amount")
    #Check if the item already exists or not
    if product in items:
        raise exception.ItemExists("Item {} already exists".format(name))
    else: items.append(product)