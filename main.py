#import local modules
import modules.PhotoFrame as PF
import modules.MusicApp as MP
import modules.VideoPlayer as VP
import utils.settingHandler as SH

#import python modules
import tkinter as tk
from tkinter import ttk
import logging
import sys


class MenuSystem:
    def __init__(self, root, ProgramSettings):
        self.root = root
        self.modules = {
            'Digital Photo Frame': PF.DigitalPhotoFrame(self, ProgramSettings),
            'Music Player': MP.MusicPlayer(self.root),
            'Video Player': VP.VideoPlayer(self.root)
        }
        self.current_module = None

        self.create_ui()
        self.root.bind('<Escape>', lambda event: self.close())
        self.open_module('digital_photo_frame')

    def create_ui(self):
        self.menu_frame = ttk.Frame(self.root)
        self.menu_frame.pack(fill=tk.BOTH, expand=True)
        
        button_height = self.root.winfo_screenheight() // len(self.modules)
        for module_name in self.modules:
            style = ttk.Style()
            style.configure("Custom.TButton", font=("Arial", 20), height=button_height)

            button = ttk.Button(self.menu_frame,
                                text=module_name,
                                command=lambda name=module_name: self.open_module(name),
                                style="Custom.TButton"
                                )
            
            button.pack(fill=tk.BOTH, expand=True)

    def open_module(self, module_name):
        if self.current_module:
            self.current_module.hide()

        self.current_module = self.modules.get(module_name)
        if self.current_module:
            self.current_module.show()
            self.hide_menu()

    def hide_menu(self):
        self.menu_frame.pack_forget()

    def show_menu(self):
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

    def close(self):
        sys.exit()  # if you want to exit the entire thing


if __name__ == '__main__':
    ProgramSettings = SH.loadSettings()

    logging.basicConfig(filename='photo_frame.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s:%(message)s', filemode='w')

    # Example logging usage
    logging.info("Starting Digital Photo Frame")

    root = tk.Tk()

    root.title("Raspberry Pi Multimedia App")
    root.attributes('-fullscreen', True)
    root.configure(background="black")

    menu = MenuSystem(root, ProgramSettings)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 20))

    root.mainloop()
