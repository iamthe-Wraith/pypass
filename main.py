import tkinter as tk
from tkinter import messagebox
from config import *
import random
import string
import pyperclip

window = tk.Tk()
window.title("Pymodoro")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def add_entry():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields")
        return

    with open("data.txt", "a") as file:
        file.write(f"{website}|{email}|{password}\n")

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo(title="Success", message="Entry added successfully!")

def generate_password():
    password_entry.delete(0, tk.END)
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    password_entry.insert(0, password)
    pyperclip.copy(password)

canvas = tk.Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
lock = tk.PhotoImage(file="lock.png")
canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=lock)
canvas.grid(column=1, row=0)

# row
website_label = tk.Label(text="Website:", bg=BACKGROUND_COLOR)
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=38, bg=BACKGROUND_COLOR)
website_entry.grid(column=1, row=1, columnspan=2)
# end_row

# row
email_username_label = tk.Label(text="Email/Username:", bg=BACKGROUND_COLOR)
email_username_label.grid(column=0, row=2)

email_username_entry = tk.Entry(width=38, bg=BACKGROUND_COLOR)
email_username_entry.insert(0, "example@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
# end_row

# row
password_label = tk.Label(text="Password:", bg=BACKGROUND_COLOR)
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=21, bg=BACKGROUND_COLOR)
password_entry.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", bg=BACKGROUND_COLOR, command=generate_password)
generate_button.grid(column=2, row=3)
# end_row

# row
add_button = tk.Button(window, text="Add", width=35, command=add_entry)
add_button.grid(column=1, row=4, columnspan=2)
# end_row

window.lift()
window.focus_force()
website_entry.focus()
window.mainloop()