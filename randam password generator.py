import random
import string
import tkinter as tk
from tkinter import messagebox
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=5)
entry_length = tk.Entry(root, font=("Arial", 12), width=10)
entry_length.pack(pady=5)
tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)
tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, font=("Arial", 12), width=30)
entry_password.pack(pady=5)
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard).pack(pady=10)
root.mainloop()
