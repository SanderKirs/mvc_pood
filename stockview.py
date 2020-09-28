class Stockview:
    def showItemsStock(self, stockItems):
        print("Stock items")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in stockItems:
            print(item.getName() + "\t|\t" +
                  str(item.getPrice()) + "\t\t|\t" +
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")

    # show item
    def showItemStock(self, item):
        print("Stock item {}".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName() + "\t|\t" +
              str(item.getPrice()) + "\t\t|\t" +
              str(item.getAmount()))
        print("---------------------------")
        print("============================")

    # no item error
    def noItemErrorStock(self, name):
        print("============================")
        print("Stock does not hold this item {}".format(name))
        print("============================")

    def ListEmptyStock(self):
        print("============================")
        print("The list is empty.")
        print("============================")

    def deleteItemStock(self, name):
        print("============================")
        print("Item {} has been deleted.".format(name))
        print("============================")

    def updateItemStock(name, price, amount):
        print("============================")
        print("Item {} now has a price of {} and there is {} of it.".format(name, price, amount))
        print("============================")