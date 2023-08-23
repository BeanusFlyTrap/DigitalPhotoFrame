#Importing Native Python Modules
import tkinter as tk
from PIL import Image, ImageTk
import os

import utils.settingHandler as settingHandler

#Defining the App as a Class, with local functions defined 
class DigitalPhotoFrame:
    def __init__(self, root, ProgramSettings):
        self.root = root
        self.root_photo_folder = ProgramSettings.get("root_photo_folder", "")

        if not self.root_photo_folder:
            self.root_photo_folder = input("Please enter a folder name")
            ProgramSettings["root_photo_folder"] = self.root_photo_folder
            settingHandler.updateSettings(ProgramSettings)
        else: 
            pass  

        self.display_duration = ProgramSettings.get("display_duration", 5) * 1000
        self.current_image_idx = 0
        self.photo_list = [file for file in os.listdir(self.root_photo_folder) if file.lower().endswith(('.jpg', '.png', '.jpeg'))]

        #generate list of photos
        self.photo_list = os.listdir(self.root_photo_folder) #Creates a list of files in the folder provided -> this needs to be filtered for image files as it will allow the removal of handling for incompatible files
        
        self.label = tk.Label( root, \
                               borderwidth=0 )
        self.label.place( relx=0.5, \
                          rely=0.5, \
                          anchor="center" )
        
        #defining click event to open the settings Gui
        self.root.bind('<Button-1>', lambda event: self.open_settings())

        # Bind a keyboard shortcut (e.g., 's') to open settings
        self.root.bind('s', lambda event: self.open_settings())

        #self.label.pack()
        self.update_image()

    def update_image(self):
        try:
            maxheight = int(self.root.winfo_screenheight())
            maxwidth = int(self.root.winfo_screenwidth())
            WinSize = (maxwidth, maxheight)

            photo_path = os.path.join(self.root_photo_folder, self.photo_list[self.current_image_idx])
            photo = Image.open(photo_path)
            photo.thumbnail(WinSize)
            converted_photo = ImageTk.PhotoImage(photo)
            
            self.label.configure(image=converted_photo)
            self.label.image=converted_photo
            
            self.current_image_idx = (self.current_image_idx + 1) % len(self.photo_list)
            self.root.after(self.display_duration, self.update_image)

        except Exception as e:
            #do nothing
            print(e)
            self.current_image_idx = (self.current_image_idx + 1) % len(self.photo_list)
            self.root.after(self.display_duration, self.update_image)

    def open_settings(self):
        print("Settings opened")

if __name__ == '__main__':
    #import settings
    ProgramSettings = settingHandler.loadSettings()

    #application setup and run
    root = tk.Tk()
    root.title("Digital Photo Frame")
    root.attributes('-fullscreen', True)
    root.configure(background="black")

    app = DigitalPhotoFrame(root, ProgramSettings)

    root.mainloop()

    #program cleanup
