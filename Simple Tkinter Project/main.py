from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(row=0, column=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button2 = Button(text="Click Me 2", command=button_clicked)
button2.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=2, column=3)
print(input.get())

window.mainloop()
