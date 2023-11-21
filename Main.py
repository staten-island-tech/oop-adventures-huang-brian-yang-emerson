import DialogueService, SaveService, EventService, SequenceService

def Main():
    SaveID = SequenceService.MainMenu()
    SequenceService.tutorial()

Main()