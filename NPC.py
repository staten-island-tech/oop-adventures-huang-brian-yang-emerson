class Shop:
    def __init__(self,name,items,costs):
        self.name = name
        self.items = items
        self.costs = costs
    def intro(self,name):
        print("Hey, it's ya boi! Care to look into my inventory?")

Emerson = Shop("Emerson",["Apple","Banana"],[5,5])
