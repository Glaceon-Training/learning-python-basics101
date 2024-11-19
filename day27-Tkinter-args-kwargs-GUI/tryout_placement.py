import tkinter as tk

"""
>>> pack() vs place() vs grid():
1) pack(): packs widget next to each other, if default starts from top center down to bottom.
        If left packs from left center to right next to each other.
2) place(): place requires detailed x and y to put the widget in position inside window.
3) grid(): place widgets in grid-mannered window consists of ROW and COLUMNS.

--Only one placement system can be used, if 2 widgets already used grid() then the window placement system is grid(),
    you can not use pack() on 3rd widget or else it will return error.
"""

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add padding to window, so widget did not stick to the edge of window
window.config(padx=20, pady=20)

def button_action():
    get_it = my_entry.get()
    my_label.config(text=get_it)


# Label
my_label = tk.Label(text="New Text", font=("Arial", 18, "normal"))
my_label.grid(row=0, column=0)
# We can also add padding to specific widget to give space from one widget to another
my_label.config(padx=30, pady=30)

# Button 1
button1 = tk.Button(text="Click Me 1")
button1.grid(row=1, column=1)

# Button 2
button2 = tk.Button(text="Click Me 2")
button2.grid(row=0, column=2)

# Entry
my_entry = tk.Entry(width=20)
my_entry.grid(row=2, column=3)

window.mainloop()
