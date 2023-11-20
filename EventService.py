import SaveService, json


def Event(Day, SaveID):
    Data = SaveService.GetSave(SaveID)
    print(Data)


