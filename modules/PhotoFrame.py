#Importing Native Python Modules
import tkinter as tk
import random
from PIL import Image, ImageTk
import os

#Defining the App as a Class, with local functions defined 
class DigitalPhotoFrame:
    def __init__(self, parent, ProgramSettings):
        #Defning program parent and instantiation of layout variables
        self.parent = parent.root
        self.parent_frame = parent
        self.frame = None
        self.label = None

        #instatiating and defining key variables from settings such as root folder and image index
        self.root_photo_folder = ProgramSettings.get("root_photo_folder", "")
        self.display_duration = ProgramSettings.get("display_duration", 5) * 1000
        self.current_image_idx = 0
        self.photo_list = [file for file in os.listdir(self.root_photo_folder) if file.lower().endswith(('.jpg', '.png', '.jpeg'))]

        #generate list of photos
        self.photo_list = os.listdir(self.root_photo_folder) #Creates a list of files in the folder provided -> this needs to be filtered for image files as it will allow the removal of handling for incompatible files
        random.shuffle(self.photo_list)
        #defining click event to open the settings Gui
        self.parent.bind('<Button-1>', lambda event: self.hide())

        self.update_image()

    def update_image(self):
        try:
            maxheight = int(self.parent.winfo_screenheight())
            maxwidth = int(self.parent.winfo_screenwidth())
            WinSize = (maxwidth, maxheight)

            photo_path = os.path.join(self.root_photo_folder, self.photo_list[self.current_image_idx])
            photo = Image.open(photo_path)
            photo.thumbnail(WinSize)
            converted_photo = ImageTk.PhotoImage(photo)
            
            self.label.configure(image=converted_photo)
            self.label.image=converted_photo
            
            self.current_image_idx = (self.current_image_idx + 1) % len(self.photo_list)
            self.parent.after(self.display_duration, self.update_image)

        except Exception as e:
            #do nothing
            print(e)
            self.current_image_idx = (self.current_image_idx + 1) % len(self.photo_list)
            self.parent.after(self.display_duration, self.update_image)

    #Definre the Layout of the PhotoFrame Window
    def create_ui(self):
        self.frame = tk.Frame(self.parent, background="black")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, borderwidth=0)
        self.label.place(relx=0.5, rely=0.5, anchor="center")

    #Runs the setup for when the show function is called
    def show(self):
        self.create_ui()
        self.update_image()

    #Closes the Window to bring back up the menu when screen is clicked
    def hide(self):
        if self.frame:
            self.frame.destroy()
            self.frame = None
            self.parent_frame.show_menu()

