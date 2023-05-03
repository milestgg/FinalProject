# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 22:40:32 2023

@author: Miles Tran
"""

from tkinter import *

# Create a new window
root = Tk()
root.title("Number Selector")

# Create a label
label = Label(root, text="Select a number between 1 and 50:")
label.pack()

# Create a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a listbox to hold the numbers
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(1, 51):
    listbox.insert(END, i)

listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=listbox.yview)

# Set the default value to 1
listbox.selection_set(0)

# Function to get the selected value
def get_selected():
    selected = listbox.curselection()
    if selected:
        value = listbox.get(selected[0])
        print("Selected value:", value)

# Create a button to get the selected value
button = Button(root, text="Get Selected Value", command=get_selected)
button.pack()

# Run the main loop
root.mainloop()
