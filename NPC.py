class Shop:
    def __init__(self,name,items,costs):
        self.name = name
        self.items = items
        self.costs = costs
    def intro(self,name):
        print("Hello, wanderer! I'm "+name+"! Would you like to look into my inventory?")
    def GiveShopInventory(self,items,costs):
        print("Inventory")
        for i in range(len(items)):
            print("||    "+items[i]+": "+str(costs[i])+"G")
    def Buy(self,items,boughtItem):
        print("You bought "+boughtItem+".")
        items.pop(boughtItem)
        self.items = items

Emerson = Shop("Emerson",["Apple","Banana"],[5,5])

Emerson.intro(Emerson.name)

Emerson.GiveShopInventory(Emerson.items, Emerson.costs)

