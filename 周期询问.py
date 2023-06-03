import tkinter as tk
import time
import datetime
from tkinter import simpledialog
import pygetwindow as gw  
# create the main window
root = tk.Tk()

# 检查是否有对应标题的窗口，有，等10分
def check_window(title,dialog):
    # print(title in gw.getAllTitles())
    while True:
        try:
            dialog.destroy()
            break
        except:
            print("Something else went wrong")
    
    if (title == ""):
        # print(1)
        get_input()
    elif any(title in t for t in gw.getAllTitles()):
        print(datetime.datetime.now(),title)
        
        root.after(60*1000*10,lambda:get_input())
    else:
        # print(3)
        get_input()
    
def get_input():
    
    # create a new window for the input dialog
    dialog = tk.Toplevel(root)

    # set the title and geometry of the window
   
    dialog.geometry("200x100")

    # create a label, an input
    label = tk.Label(dialog, text="在做什么:")
    entry = tk.Entry(dialog)
    
    entry.bind("<Return>",  lambda event:check_window(entry.get(),dialog))
    
    
        
    entry.after(60*1000,lambda :check_window(entry.get(),dialog))
    # gain focus tkinter
    
    
    dialog.state("zoomed")
    
    
    # add the label, the text field, and the button to the window
    label.pack()
    
    entry.pack()
    
    
    # raise the window to the top of the stacking order and make it stay on top
    dialog.lift()
    dialog.attributes("-topmost", True)
    
    entry.focus_set()   
# define a function that is called when the focus is lost

# create a button that prompts the user for input
get_input()

# start the main event loop
root.mainloop()