import os, time

class Shop:
    def __init__(self,name,items,costs):
        self.name = name
        self.items = items
        self.costs = costs
    def intro(self):
        print("Hello, wanderer! I'm "+self.name+"! Would you like to look into my inventory?")
        time.sleep(3)
    def GiveShopInventory(self):
        os.system("cls")
        print("Inventory:")
        for i in range(len(self.items)):
            if i == Selected:
                print("|| ==> "+self.items[i]+": "+str(self.costs[i])+"G")
            else:
                print("||     "+self.items[i]+": "+str(self.costs[i])+"G")
        
        print()

        print("╔═════════════════════╗")
        print("║  W/S        Up/Down ║")
        print("║  A           Select ║")
        print("╚═════════════════════╝")
    def Buy(self, boughtItem):
        buying = input("Buy "+boughtItem+"? (Y/N) ")
        buying = buying.upper()
        if buying == "Y":
            os.system("clr")
            print("You bought "+boughtItem+".")
            self.items.remove(boughtItem)
            self.items = self.items
            time.sleep(3)
    def NavigateShop(self,Selected):
        Navigate = input()
        Navigate = Navigate.upper()

        if Navigate == "W":
            if not Selected < 0:
                Selected -= 1
            else:
                Selected = len(self.items)
        if Navigate == "S":
            if not Selected > len(self.items)-2:
                Selected += 1
            else:
                Selected = 0
        if Navigate == "A":
            self.Buy(self.items[Selected])
        
        return Selected


Emerson = Shop("Emerson",["Apple","Banana","Final-Stand Potion"],[5,5,100])

Emerson.intro()

Selected = 0


for i in range(100):
    print(Selected)
    Emerson.GiveShopInventory()
    Selected = Emerson.NavigateShop(Selected)
