import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def clear_tasks():
    listbox_tasks.delete(0, tk.END)
root = tk.Tk()
root.title("🌟 Colorful To-Do List")
root.geometry("450x500")
root.config(bg="#F4D03F")  
font_style = ("Arial", 12, "bold")
btn_bg_color = "#48C9B0"  
btn_fg_color = "white"
tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"), bg="#F4D03F").pack(pady=10)
entry_task = tk.Entry(root, font=font_style, width=30, bd=2, relief=tk.SOLID)
entry_task.pack(pady=10)
tk.Button(root, text="➕ Add Task", font=font_style, bg=btn_bg_color, fg=btn_fg_color, command=add_task).pack(pady=5)
tk.Button(root, text="❌ Delete Task", font=font_style, bg="#E74C3C", fg="white", command=delete_task).pack(pady=5)
tk.Button(root, text="🗑️ Clear All", font=font_style, bg="#3498DB", fg="white", command=clear_tasks).pack(pady=5)
listbox_tasks = tk.Listbox(root, font=font_style, width=40, height=10, bg="white", fg="black", selectbackground="#F39C12")
listbox_tasks.pack(pady=10)
root.mainloop()
import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def clear_tasks():
    listbox_tasks.delete(0, tk.END)
root = tk.Tk()
root.title("🌟 Colorful To-Do List")
root.geometry("450x500")
root.config(bg="#F4D03F")  
font_style = ("Arial", 12, "bold")
btn_bg_color = "#48C9B0"  
btn_fg_color = "white"
tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"), bg="#F4D03F").pack(pady=10)
entry_task = tk.Entry(root, font=font_style, width=30, bd=2, relief=tk.SOLID)
entry_task.pack(pady=10)
tk.Button(root, text="➕ Add Task", font=font_style, bg=btn_bg_color, fg=btn_fg_color, command=add_task).pack(pady=5)
tk.Button(root, text="❌ Delete Task", font=font_style, bg="#E74C3C", fg="white", command=delete_task).pack(pady=5)
tk.Button(root, text="🗑️ Clear All", font=font_style, bg="#3498DB", fg="white", command=clear_tasks).pack(pady=5)
listbox_tasks = tk.Listbox(root, font=font_style, width=40, height=10, bg="white", fg="black", selectbackground="#F39C12")
listbox_tasks.pack(pady=10)
root.mainloop()
