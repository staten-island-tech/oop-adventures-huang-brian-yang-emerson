class Shop:
    def __init__(self,name,items,costs):
        self.name = name
        self.items = items
        self.costs = costs
    def intro(name):
        print("Hey, it's ya boi "+name+"! Care to look into my inventory?")
    def sell(items,costs):
        print("Hey~~~ o///v///o")

Emerson = Shop("Emerson",["Apple","Banana"],[5,5])

Shop.intro(Emerson.name)
