import modules.PhotoFrame as PF
import tkinter as tk
from tkinter import ttk

class MenuSystem:
    def __init__(self, root):
        self.root = root

        self.modules = {
            'photo_frame': PF.DigitalPhotoFrame(root, ProgramSettings)
            # Add more modules as needed
        }

        self.open_module('photo_frame')

    def open_module(self, module_name):
        # Hide all modules except the specified one
        for name, module in self.modules.items():
            if name == module_name:
                module.label.place(relx=0.5, rely=0.5, anchor="center")
            else:
                module.label.place_forget()

        # Hide or disable other widgets here
        # For example, you can use widget.place_forget() or widget.config(state="disabled")


if __name__ == '__main__':
    ProgramSettings = {}  # Load your settings here

    root = tk.Tk()
    root.title("Digital Photo Frame")
    root.attributes('-fullscreen', True)
    root.configure(background="black")

    menu_system = MenuSystem(root)

    # Create themed buttons for menu navigation using ttk
    photo_frame_button = ttk.Button(root, text="Photo Frame", style="TButton",
                                    command=lambda: menu_system.open_module('photo_frame'))
    # Add more buttons for other modules

    photo_frame_button.place(relx=0.5, rely=0.9, anchor="center")
    # Position other buttons as needed

    # Create a themed style for the buttons
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 20))

    root.mainloop()
