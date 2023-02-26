import tkinter as tk
from tkinter import simpledialog

# create the main window
root = tk.Tk()

# define a function that prompts the user for input
def get_input():
    # create a new window for the input dialog
    dialog = tk.Toplevel(root)

    # set the title and geometry of the window
    dialog.title("Input")
    dialog.geometry("200x100")

    # create a label, a text field, and a button
    label = tk.Label(dialog, text="Please enter some text:")
    entry = tk.Entry(dialog)
    button = tk.Button(dialog, text="OK", command=dialog.destroy)

    # add the label, the text field, and the button to the window
    label.pack()
    entry.pack()
    button.pack()

    # raise the window to the top of the stacking order and make it stay on top
    dialog.lift()
    dialog.attributes("-topmost", True)

# create a button that prompts the user for input
button = tk.Button(root, text="Click me", command=get_input)
button.pack()

# start the main event loop
root.mainloop()