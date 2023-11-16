import SaveService

def Event(Day, SaveID):
    Data = SaveService.GetSave(SaveID)
    print(Data)

