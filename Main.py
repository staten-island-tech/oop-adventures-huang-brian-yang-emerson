import DialogueService, SaveService, EventService, SequenceService, time

def Main():
    SaveID = SequenceService.MainMenu()
    print(SaveService.GetSave(SaveID))
    SequenceService.tutorial()

Main()