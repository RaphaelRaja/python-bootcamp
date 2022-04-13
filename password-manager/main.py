from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry()
email_username_input.grid(row=2, column=1, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
