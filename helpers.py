import exceptions
from product import Product

# represesents shop structure
# list of Product type objects
items = []
stockItems = []

#-------Shop-------#

#Add an item
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control if item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} already exists".format(name))
    else:
        items.append(product)

#Show all items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return items

#Show a single item
def showItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))

#Delete a single item
def deleteItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            items.remove(item)
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))

#Delete all items
def deleteAllItems():
    global items
    items.clear()

#Update an item
def updateItem(name, price, amount):
    global items

    isUpdated = False
    # check all of the items one by one
    for item in items:
        # if the name matches our search
        if(item.getName() == name):
            # update the item
            item.setPrice(price)
            item.setAmount(amount)
            isUpdated = True
        else:
            continue
    if (isUpdated != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))


#-------Stock-------#

stockItems = []

#Add an item to the stock
def addItemStock(name, price, amount):
    global stockItems
    # create product with reqiure description
    product = Product(name, price, amount)
    # control if item already exists
    if product in stockItems:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        stockItems.append(product)

#Show the items in stock
def showItemsStock():
    global stockItems
    # control if items exists
    if len(stockItems) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return stockItems

#Show an item that is in stock
def showItemStock(name):
    global stockItems
    # control all items step by step
    for item in stockItems:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))

#Delete's an item in the stock
def deleteItemStock(name):
    global stockItems
    # control all items step by step
    for item in stockItems:
        # if the name is the same as we search
        if(item.getName() == name):
            stockItems.remove(item)
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))

#Delete's all items in stock
def deleteAllItemsStock():
    global stockItems
    stockItems.clear()

#Updates an item in stock
def updateItemStock(name, price, amount):
    global stockItems
    isUpdated = False
    # check all of the items one by one
    for item in stockItems:
        # if the name matches our search
        if(item.getName() == name):
            # update the item
            item.setPrice(price)
            item.setAmount(amount)
            isUpdated = True
        else:
            continue
    if (isUpdated != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))

#Adds items to the shop from the stock
def addFromStock(name, price, takeAmount):
    global items
    global stockItems
    global updateItemStock
    global addItem

    for item in stockItems:
        # if the name matches our search
        if(item.getName() == name):
            newStockAmount = (item.getAmount() - takeAmount)
            item.setAmount(newStockAmount)
            continue
        else:
            continue
            raise exceptions.ItemNotExists("Item {} doesn't exist in stock".format(name))

    for thing in items:
        # if the name matches our search
        if (thing.getName() == name):
            totalAmount = thing.getAmount() + takeAmount
            thing.setPrice(price)
            thing.setAmount(totalAmount)
            break
        else:
            product = Product(name, price, takeAmount)
            if product in items:
                print("Error: Item {} already exists".format(name))
            else:
                items.append(product)
            break
    for item in stockItems:
        if item.getAmount() <= 0:
            deleteItemStock(item.getName())