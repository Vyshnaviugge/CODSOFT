import tkinter as tk
from tkinter import messagebox
def on_button_click(value):
    if value == "C":
        entry_var.set("")  
    elif value == "⌫":
        entry_var.set(entry_var.get()[:-1])
    elif value == "=":
        try:
            result = eval(entry_var.get()) 
            entry_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            entry_var.set("")
        except Exception:
            messagebox.showerror("Error", "Invalid input!")
            entry_var.set("")
    elif value == "Dark Mode":
        root.config(bg="#2C3E50")
        entry.config(bg="#1E1E1E", fg="white")
        frame.config(bg="#2C3E50")
    elif value == "Light Mode":
        root.config(bg="#FDEBD0")
        entry.config(bg="white", fg="black")
        frame.config(bg="#FDEBD0")
    else:
        entry_var.set(entry_var.get() + value)
root = tk.Tk()
root.title("🎨 Colorful Calculator")
root.geometry("350x500")  
root.config(bg="#FDEBD0") 
btn_font = ("Arial", 14, "bold")
btn_colors = {
    "numbers": "#48C9B0",  
    "operations": "#3498DB", 
    "special": "#E74C3C",  
    "mode": "#F39C12"  
}
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=5, relief=tk.FLAT, bg="white", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)
buttons = [
    ("C", "⌫", "/", "*"),
    ("7", "8", "9", "-"),
    ("4", "5", "6", "+"),
    ("1", "2", "3", "="),
    ("0", ".", "Dark Mode", "Light Mode")
]
frame = tk.Frame(root, bg="#FDEBD0")
frame.pack()
for row in buttons:
    row_frame = tk.Frame(frame, bg="#FDEBD0")
    row_frame.pack(fill="both", expand=True)
    for btn_text in row:
        btn_color = (
            btn_colors["numbers"] if btn_text.isdigit() or btn_text == "."
            else btn_colors["operations"] if btn_text in "+-*/"
            else btn_colors["special"] if btn_text in ["C", "⌫", "="]
            else btn_colors["mode"]
        )
        btn_width = 6 if btn_text in "+-*/=" else 4  
        btn = tk.Button(
            row_frame, text=btn_text, font=btn_font, bg=btn_color, fg="white",
            width=btn_width, height=2,
            command=lambda value=btn_text: on_button_click(value)
        )
        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)
root.mainloop()
