
# Import the Required Modules
import tkinter as tk #Used for the Main Display Output
from PIL import Image, ImageTk #Used for Image Handling / Re-sizing
import os #Used for Image file Handling

class App():
    def __init__(self):
        self.root = tk.Tk()
        
        self.root_photo_folder = input("Please enter a folder name") #Change to update config file of some description in future
        self.photo_list = os.listdir(self.root_photo_folder) #Creates a list of files in the folder provided -> this needs to be filtered for image files as it will allow the removal of handling for incompatible files
        self.photoCounter = 0 #Acts as a pointer for the image on screen
        while True: #Handles potential files incompatible with the image
            try: 
                initial_photo = Image.open((self.root_photo_folder+"\\"+self.photo_list[self.photoCounter]))
                converted_photo = ImageTk.PhotoImage(initial_photo)
                break
            except Exception as e:
                self.photoCounter += 1
                if self.photoCounter == len(self.photo_list):
                    self.photoCounter = 0
                else:
                    pass
                # No other condition needed
                print(e)


        self.label = tk.Label(image=converted_photo, \
                              borderwidth=0           )
        self.label.place(relx=0.5,      \
                         rely=0.5,      \
                         anchor="center" ) #Centers the image in the window

        #self.label.pack()
        self.update_image()
        self.root.wm_attributes("-fullscreen", "True")
        self.root.configure(background="black")
        self.root.mainloop()

    def update_image(self):
        try:
            maxheight = int(self.root.winfo_screenheight())
            maxwidth = int(self.root.winfo_screenwidth())
            WinSize = (maxwidth, maxheight)

            photo = Image.open((self.root_photo_folder+"\\"+self.photo_list[self.photoCounter]))
            photo.thumbnail(WinSize)
            converted_photo = ImageTk.PhotoImage(photo)
            
            self.label.configure(image=converted_photo)
            self.label.image=converted_photo
            self.photoCounter +=1
            if self.photoCounter == len(self.photo_list):
                self.photoCounter = 0
            else:
                pass
                # No other condition needed
                 
            self.root.after(3000, self.update_image)

        except Exception as e:
            #Attempt to Move to next file (hopefully an image one)
            print(e)
            self.photoCounter +=1
            self.root.after(100, self.update_image)

if __name__ == '__main__':
    app=App()

