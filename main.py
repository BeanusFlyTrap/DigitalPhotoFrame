#this file dont work yet

import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
import os

def resize_ratio(max_height, height):
    ratio = min(max_height/height)
    return (height)


class App():
    def __init__(self):
        self.root = tk.Tk()
        
        self.root_photo_folder = "<Insert foldername here>"
        self.photo_list = os.listdir(self.root_photo_folder)
        self.photoCounter = 0
        initial_photo = Image.open((self.root_photo_folder+"\\"+self.photo_list[self.photoCounter]))
        converted_photo = ImageTk.PhotoImage(initial_photo)

        

        self.label = tk.Label(image=converted_photo)

        self.label.pack()
        self.update_image()
        self.root.wm_attributes("-fullscreen", "True")
        self.root.configure(background="black")
        self.root.mainloop()
    def update_image(self):
        try:
            photo = Image.open((self.root_photo_folder+"\\"+self.photo_list[self.photoCounter]))
            (width, height) = photo.size
            print("Height: {}, Width: {}".format(height, width))
            maxheight = int(self.root.winfo_screenheight())
            maxwwidth = int(self.root.winfo_screenwidth())
            print("maxHeight: {}, maxWidth: {}".format(maxheight, maxwwidth))
            if ((height > maxheight) or (width > maxwwidth)):
                ratio = min(width/maxwwidth, height/maxheight)
                print(ratio)
                resized_photo = photo.resize((int(height*ratio),int(width*ratio)), Image.BILINEAR )
                converted_photo = ImageTk.PhotoImage(resized_photo)
                self.label.configure(image=converted_photo)
                self.label.image=converted_photo
                self.photoCounter +=1
                self.root.after(1000, self.update_image)
            else:            
                converted_photo = ImageTk.PhotoImage(photo)
                self.label.configure(image=converted_photo)
                self.label.image=converted_photo
                self.photoCounter +=1
                self.root.after(1000, self.update_image)
        except Exception as e:
            #do nothing
            print(e)
            self.photoCounter +=1
            self.root.after(3000, self.update_image)

app=App()

