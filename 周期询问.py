import tkinter as tk
import time
from tkinter import simpledialog
import pygetwindow as gw  
# create the main window
root = tk.Tk()

# define a function that prompts the user for input
def check_window(title,dialog):
    print(title)
    dialog.destroy()
    if (title == ""):
        get_input()
    elif (title in gw.getAllTitles()):
        dialog.destroy()
        time.sleep(5*60)
        get_input()
    
def get_input():
    # create a new window for the input dialog
    dialog = tk.Toplevel(root)

    # set the title and geometry of the window
   
    dialog.geometry("200x100")

    # create a label, a text field, and a button
    label = tk.Label(dialog, text="在做什么:")
    entry = tk.Entry(dialog)
    button = tk.Button(dialog, text="OK", command=lambda:check_window(entry.get(),dialog))
        
    # add the label, the text field, and the button to the window
    label.pack()
    entry.pack()
    button.pack()

    # raise the window to the top of the stacking order and make it stay on top
    dialog.lift()
    dialog.attributes("-topmost", True)
# define a function that is called when the focus is lost

# create a button that prompts the user for input
get_input()

# start the main event loop
root.mainloop()