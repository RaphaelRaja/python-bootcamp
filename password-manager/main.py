from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_input.insert(0, password)
    password_input.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        new_data = {website: {
            "email": email_username,
            "password": password,
        }}

        def write_file(dataforfile):
            with open("data.json", "w") as f:
                json.dump(dataforfile, f, indent=4)
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')
                website_input.focus()

        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            write_file(new_data)
        else:
            write_file(data)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            get_email_password = data[website]
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No Data file found")
    except KeyError:
        messagebox.showinfo(title="Oops!", message=f"No details for {website} exists.")
    else:
        email = get_email_password["email"]
        password = get_email_password["password"]
        messagebox.showinfo(title=website, message=f"Email:{email}\n Password: {password}")


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
website_input.grid(row=1, column=1, sticky="EW")
website_input.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry()
email_username_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_input.insert(0, "jrrphonix@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
