from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}"
                                                          f" \nPassword: {password} \n Is it ok to save?")

    data = website + " | " + email_username + " | " + password + "\n"

    if is_ok:
        with open("data.txt", "a") as f:
            f.write(data)
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry()
email_username_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_input.insert(0, "jrrphonix@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
