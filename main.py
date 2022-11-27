from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 & len(password) == 0:
        messagebox.showinfo(title="oops", message="These field are empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered: "
                                                              f"\nEmail: {username}\n Password: {password}\n" f" is "
                                                              "it ok "
                                                              "to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  | {username}  |  {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky=EW)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky=EW)
username_input.insert(0, "lokesharya78@gmail.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3, sticky=W)

generate_password_btn = Button(text="Generate Password", bg="White", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky=EW)

add_btn = Button(text="Add", width=30, bg="White", command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()
