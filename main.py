#this file dont work yet

import tkinter as tk
from tkinter import PhotoImage


def window(imagepath):
    window = tk.Tk()
    photoImage = PhotoImage(file = imagepath)
    label = tk.Label(window, image = photoImage)
    label.pack()
    window.mainloop()

window("C:/Users/darth/Pictures/Wallpapers/Taiga.jpg")

#root.wm_attributes('-fullscreen', 'True')
#root.mainloop()
