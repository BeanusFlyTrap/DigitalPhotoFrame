#Import Custom modules
import settingHandler

#Importing Native Python Modules
import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
import os

#Defining the App as a Class, with local functions defined 
class DigitalPhotoFrame:
    def __init__(self, root, ProgramSettings):
        self.root = root

        #check root folder is set in settings
        if ProgramSettings["root_photo_folder"] == "" :
            ProgramSettings["root_photo_folder"] = input("Please enter a folder name") #Change to update config file of some description in future
            settingHandler.updateSettings(ProgramSettings)
        else: 
            #No alternative condition needed 
            
            pass
        
        self.root_photo_folder = ProgramSettings["root_photo_folder"]
        self.display_duration = ProgramSettings["display_duration"] * 1000
        self.current_image_idx = 0

        #generate list of photos
        self.photo_list = os.listdir(self.root_photo_folder) #Creates a list of files in the folder provided -> this needs to be filtered for image files as it will allow the removal of handling for incompatible files
        while True: #Handles potential files incompatible with the image
            try: 
                initial_photo = Image.open((self.root_photo_folder+"\\"+self.photo_list[self.current_image_idx]))
                converted_photo = ImageTk.PhotoImage(initial_photo)
                break
            except Exception as e:
                self.current_image_idx += 1
                if self.current_image_idx == len(self.photo_list):
                    self.current_image_idx = 0
                else:
                    pass
                # No other condition needed
                print(e)


        self.label = tk.Label(image=converted_photo, \
                              borderwidth=0           )
        self.label.place(relx=0.5,      \
                         rely=0.5,      \
                         anchor="center" ) #Centers the image in the window
        
        #defining a button to open the settings Gui, this also includes a keyboard shortcut
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

            photo = Image.open((self.root_photo_folder+"\\"+self.photo_list[self.current_image_idx]))
            photo.thumbnail(WinSize)
            converted_photo = ImageTk.PhotoImage(photo)
            
            self.label.configure(image=converted_photo)
            self.label.image=converted_photo
            self.current_image_idx +=1
            if self.current_image_idx == len(self.photo_list):
                self.current_image_idx = 0
            else:
                pass
                # No other condition needed
                 
            self.root.after(self.display_duration, self.update_image)

        except Exception as e:
            #do nothing
            print(e)
            self.current_image_idx +=1
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
