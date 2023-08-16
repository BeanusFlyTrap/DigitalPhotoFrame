import os

#Checks if Settings file exists, creates a blank one if not
def ensureSettingsExists():
    if not(os.path.isfile("settings.txt")):
        f = open("settings.txt", "a")
        f.close()
    else:
        #No other condition needed
        pass

#sets the root photos folder in settings
def setPhotosRoot():
    pass

#collects the root settings folder from settings
def getPhotosRoot():
    pass

