class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in items:
            print(item.getName() + "\t|\t" +
                  str(item.getPrice()) + "\t\t|\t" +
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")

    # show item
    def showItem(self, item):
        print("Shop item {}".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName() + "\t|\t" +
              str(item.getPrice()) + "\t\t|\t" +
              str(item.getAmount()))
        print("---------------------------")
        print("============================")

    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop does not hold this item {}".format(name))
        print("============================")

    def ListEmpty(self):
        print("============================")
        print("The list is empty.")
        print("============================")

    def deleteItem(self, name):
        print("============================")
        print("Item {} has been deleted.".format(name))
        print("============================")

    def updateItem(name, newname, newprice, newamount):
        print("============================")
        print("Item {} now has a price of {} and there is {} of it.".format(newname,newprice,newamount))
        print("============================")