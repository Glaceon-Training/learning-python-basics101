import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def button_action():
    miles = float(entry.get())
    km = miles * 1.609
    km_label.config(text=km)


# Label
label1 = tk.Label(text="is equal to")
label1.grid(row=1, column=0)
label1.config(padx=10, pady=0)

label2 = tk.Label(text="Miles")
label2.grid(row=0, column=2)
label2.config(padx=10, pady=10)

km_label = tk.Label(text=0)
km_label.grid(row=1, column=1)

label4 = tk.Label(text="Km")
label4.grid(row=1, column=2)
label4.config(padx=10, pady=10)

# Entry
entry = tk.Entry(width=10)
entry.grid(row=0, column=1)

# Button
button = tk.Button(text="Calculate", command=button_action)
button.grid(row=2, column=1)


window.mainloop()
