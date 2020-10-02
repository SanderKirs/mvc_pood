import exceptions
from product import Product

# repsresents shop structure
# list of Product type objects
items = []
stockItems = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control if item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} already exists".format(name))
    else:
        items.append(product)

# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return items
# show item
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

#delete all items
def deleteAllItems():
    global items
    items.clear()

#updates a single item
def updateItem(name, price, amount):
    global items
    print("kontroller update item fn")
    print(items)
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

# add item to items
def addItemStock(name, price, amount):
    global stockItems
    # create product with reqiure description
    product = Product(name, price, amount)
    # control if item already exists
    if product in stockItems:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        stockItems.append(product)

# show items
def showItemsStock():
    global stockItems
    # control if items exists
    if len(stockItems) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return stockItems
# show item
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

#delete all items
def deleteAllItemsStock():
    global stockItems
    stockItems.clear()

#updates a single item
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
            print("-_--_--_--_--_--_--_--_--_--_--_--_-")
            thing.setPrice(price)
            thing.setAmount(totalAmount)
        else:
            product = Product(name, price, takeAmount)
            if product in items:
                print("midagi läks nagu vussi")
            else:
                items.append(product)
            break
