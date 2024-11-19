from tkinter import *

# Creating a new window and configuration
window = Tk()
window.title("G - Widget Examples")
window.minsize(width=500, height=500)

# Label
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

# Button
def button_action():
    print("Button clicked")

button = Button(text="Click Me", command=button_action)
button.pack()

# Entry
entry = Entry(width=30)
# Insert text inside entry widget:
# Everything before first character is 0 index, everything after last character is END tk constant/"end" index.
entry.insert(0, string="hello")
entry.insert(END, string="world")
entry.insert(5, string=" , ")
# Get text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Put cursor in text widget, so we can immediately type
text.focus()
# Insert text in text widget
# When I try index 0, it returns error. But with END it returns normal.
text.insert(END, chars="Example of multi-line text entry. You can insert any words you want.")
# Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_action():
    # Get the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_action)
spinbox.pack()

# Scale
def scale_action(value):
    # Get current scale value, called with current scale value
    print(value)

scale = Scale(from_=0, to=100, command=scale_action)
scale.pack()

# Checkbutton
def checkbutton_action():
    # Print 1 if button is ON, 0 if OFF.
    print(checked_state.get())

# Variable to hold on checked state using IntVar method, 0 is off, 1 is on.
checked_state = IntVar()
# Summoning checkbutton, the text is "Is On?", variable that tracks checked state using "checked_state",
# command to print current checked state using function "checkbutton_action".
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_action)
# Get the current check state
checked_state.get()
checkbutton.pack()

# Radio Button
def radiobutton_action():
    print(radio_state.get())
# Variable to hold on which radio button is ON using IntVar, 1 is Radio Button 1, 2 is Radio Button 2.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radiobutton_action)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radiobutton_action)
radiobutton1.pack()
radiobutton2.pack()

"""
>>> Check button VS Radio button:
Check button only have 0 and 1 value, whether its on or off. Meanwhile, radio button can have various value
depends on what you give for the button. Just like the sample above, we set radio button 1 to have value 1,
and radio button 2 to have value 2. Therefore, when radio_state get printed, the value will show 1 or 2.
"""

# Listbox
def listbox_action(event):
    # Get current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=6)
# Choices of lists
fruits = ["Apple", "Pear", "Orange", "Banana"]

# Looping to get every item in list
for item in fruits:
    # Insert list item, putting the item based on its index by list and using that index for the index position
    # in INSERT method:
    # 1) "Apple" is at index 0 in list, therefore it will be INSERTED at index 0 with Apple as the item shown,
    # 2) "Pear" is at index 1 in list, therefore it will be INSERTED at index 1 with Pear as the item shown, and so on.
    listbox.insert(fruits.index(item), item)

# To execute a function when the selected items change, you bind that function to the <<ListboxSelect>> event
listbox.bind("<<ListboxSelect>>", listbox_action)
listbox.pack()

window.mainloop()
