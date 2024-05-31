import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation

    characters = lowercase_chars
    if use_uppercase:
        characters += uppercase_chars
    if use_digits:
        characters += digit_chars
    if use_special:
        characters += special_chars

    password = random.choice(lowercase_chars)
    password += random.choice(uppercase_chars) if use_uppercase else ''
    password += random.choice(digit_chars) if use_digits else ''
    password += random.choice(special_chars) if use_special else ''

    password += ''.join(random.choice(characters) for _ in range(length - len(password)))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_and_display_password():
    length = length_var.get()
    use_uppercase = use_uppercase_var.get()
    use_digits = use_digits_var.get()
    use_special = use_special_var.get()
    password = generate_password(length, use_uppercase, use_digits, use_special)
    password_display.config(state='normal')
    password_display.delete('1.0', tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state='disabled')

root = tk.Tk()
root.title("Password Generator")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Style().configure('TButton', foreground='blue', background='lightgrey', font=('Arial', 10))
ttk.Style().configure('TCheckbutton', foreground='black', background='lightgrey', font=('Arial', 10))
ttk.Style().configure('TLabel', foreground='black', background='lightgrey', font=('Arial', 10))

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
length_var = tk.IntVar(value=12)
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(row=0, column=1, sticky=tk.W, pady=(0, 5))

use_uppercase_var = tk.BooleanVar(value=True)
use_uppercase_checkbutton = ttk.Checkbutton(frame, text="Include Uppercase", variable=use_uppercase_var)
use_uppercase_checkbutton.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))

use_digits_var = tk.BooleanVar(value=True)
use_digits_checkbutton = ttk.Checkbutton(frame, text="Include Digits", variable=use_digits_var)
use_digits_checkbutton.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))

use_special_var = tk.BooleanVar(value=True)
use_special_checkbutton = ttk.Checkbutton(frame, text="Include Special Characters", variable=use_special_var)
use_special_checkbutton.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))

generate_button = ttk.Button(frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

password_display = tk.Text(frame, height=2, width=40, state='disabled', wrap='word')
password_display.grid(row=5, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
