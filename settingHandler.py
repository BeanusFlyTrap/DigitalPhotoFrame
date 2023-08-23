import os
import json

default_settings = {
    "root_photo_folder": ""
}

#Checks if Settings file exists, creates a blank one if not
def ensureSettingsExists():
    if not(os.path.isfile("settings.json")):
        with open("settings.json", "a") as settings_file:
            json.dump(default_settings, settings_file)
    else:
        #No other condition needed
        pass

#loads the settings into the program, 
#This does not need a file not found check since the file will be created beforehand if none exists
def loadSettings():
    ensureSettingsExists()
    with open("settings.json", "r") as settings_file:
        settings = json.load(settings_file)
    
    return settings

def updateSettings(new_settings):
    with open("settings.json", "w") as settings_file:
        settings = json.dump(new_settings, settings_file)
    
    pass

#sets the root photos folder in settings
def setPhotosRoot(filepath):
    pass

#collects the root settings folder from settings
def getPhotosRoot():
    pass

