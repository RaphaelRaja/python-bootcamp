from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)
miles_input.insert(END, string="0")

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

resultVar = IntVar()
result = Label(textvariable=resultVar)
result.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)


def calculate():
    miles = int(miles_input.get())
    print(miles)
    km = miles * 1.609
    resultVar.set(round(km))


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
