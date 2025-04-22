import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_random_password():
    current = ent_password.get()
    if len(current) > 0:
        overwrite = messagebox.askyesno(
            "Overwrite Password?",
            "A password already exists in the field.\n"
            "Are you sure you want to overwrite it?",
        )
        if not overwrite:
            return

    ent_password.delete(0, END)

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join([char for char in password_list])
    ent_password.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def handle_entries():
    ent_password.delete(0, "end")
    ent_website.delete(0, "end")
    ent_website.insert(END, string="e.g.: https://johndoe.com")
    ent_email.delete(0, "end")
    ent_email.insert(END, string="e.g.: contact@johndoe.com")


def save():
    website = ent_website.get()
    email = ent_email.get()
    password = ent_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields "
                                                  "empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            handle_entries()

# ---------------------------- SEARCH PASSWORD ------------------------ #
def find_password():
    website = ent_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning!", message="No data file found.")
        return

    else:
        if website in data:
            searched_website = data[website]
            messagebox.showinfo(
                title="Password found!",
                message=(
                    f"Website: {website}\n"
                    f"Email: {searched_website['email']}\n"
                    f"Password: {searched_website['password']}"
                ),
            )
        else:
            messagebox.showwarning(title="Warning!", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
# Window Frame
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas - Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
lbl_website = Label()
lbl_website.config(text="Website:", font=(FONT_NAME, 14))
lbl_website.focus()
lbl_website.grid(sticky="E", column=0, row=1)

lbl_email = Label()
lbl_email.config(text="Email/Username:", font=(FONT_NAME, 14))
lbl_email.grid(sticky="E", column=0, row=2)

lbl_password = Label()
lbl_password.config(text="Password:", font=(FONT_NAME, 14))
lbl_password.grid(sticky="E", column=0, row=3)

# Entries
ent_website = Entry(width=24, highlightthickness=0)
ent_website.insert(END, string="e.g.: https://johndoe.com")
ent_website.get()
ent_website.grid(sticky="W", column=1, row=1)

ent_email = Entry(width=43, highlightthickness=0)
ent_email.insert(END, string="e.g.: contact@johndoe.com")
ent_email.get()
ent_email.grid(sticky="W", column=1, row=2, columnspan=2)

ent_password = Entry(width=24, highlightthickness=0)
ent_password.get()
ent_password.grid(sticky="W", column=1, row=3)

# Buttons
btn_gen_password = Button(text="Generate Password", highlightthickness=0, width=15,
                          command=generate_random_password,)
btn_gen_password.grid(column=2, row=3)

btn_add = Button(text="Add", highlightthickness=0, width=40, command=save)
btn_add.grid(sticky="W", column=1, row=4, columnspan=2)

btn_search = Button(text="Search", highlightthickness=0, width=15, command=find_password)
btn_search.grid(sticky="W", column=2, row=1)


window.mainloop()
