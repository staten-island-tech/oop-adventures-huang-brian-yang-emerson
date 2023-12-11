import os

class Shop:
    def __init__(self,name,items,costs):
        self.name = name
        self.items = items
        self.costs = costs
    def intro(self):
        print("Hello, wanderer! I'm "+self.name+"! Would you like to look into my inventory?")
    def GiveShopInventory(self):
        os.system("cls")
        print("Inventory")
        for i in range(len(self.items)):
            if i == Selected:
                print("||    "+self.items[i]+": "+str(self.costs[i])+"G       <==")
            else:
                print("||    "+self.items[i]+": "+str(self.costs[i])+"G")
    def Buy(self, boughtItem):
        buying = input("Buy "+boughtItem+"? (Y/N) ")
        buying = buying.upper()
        if buying == "Y":
            print("You bought "+boughtItem+".")
            self.items.pop(boughtItem)
            self.items = self.items
    def NavigateShop(self,Selected):
        Navigate = input()
        Navigate = Navigate.upper()

        if Navigate == "W":
            Selected -= 1
        if Navigate == "S":
            Selected += 1
        return Selected


Emerson = Shop("Emerson",["Apple","Banana","Final-Stand Potion"],[5,5,100])

Emerson.intro()

Selected = 0


for i in range(10):
    Emerson.GiveShopInventory()
    Emerson.Buy(Emerson.items[Selected])
    Selected = Emerson.NavigateShop(Selected)
