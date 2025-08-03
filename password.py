import tkinter as tk
import string
import random
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        # Get password length from user input
        length = int(length_entry.get())

        characters = ""  # String to hold selected character types

        # Check which character types are selected
        if letters_var.get():
            characters += string.ascii_letters  # a-z and A-Z
        if numbers_var.get():
            characters += string.digits         # 0-9
        if symbols_var.get():
            characters += string.punctuation    # !@#$%^&*() etc.

        # If no character type is selected, show warning
        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character type.")
            return

        # Generate password by randomly choosing from selected characters
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display password on the screen
        result_label.config(text=password)

        # Copy password to clipboard
        root.clipboard_clear()
        root.clipboard_append(password)

    except ValueError:
        # If password length is not a number
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI SETUP
# Create main window
root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("350x300")
root.resizable(False, False)
# Label and Entry to get password length
tk.Label(root, text="Enter password length:", font=('Arial', 12)).pack(pady=10)
length_entry = tk.Entry(root, width=10, font=('Arial', 12))
length_entry.pack()
# Checkboxes to choose character types
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=50)
# Button to generate password
tk.Button(root, text="Generate Password", font=('Arial', 12), command=generate_password).pack(pady=20)
# Label to display the result
result_label = tk.Label(root, text="", font=('Courier', 14), fg="blue")
result_label.pack()
# Start the GUI loop
root.mainloop()
