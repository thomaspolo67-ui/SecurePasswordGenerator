import tkinter as tk
from tkinter import font, messagebox 
from password_generator import generate_password 
from tkinter import messagebox 

def generate ():

    length = int(length_entry.get()) 

    password = generate_password(
        length,
        uppercase_var.get(),
        lowercase_var.get(),
        numbers_var.get(),
        symbols_var.get()
    )
    
    if password is None:
        messagebox.showerror( 
            "Error", 
            "Please select at least two character types."
        )
        return 
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END) 
    result_entry.insert(0, password)
    result_entry.config(state="readonly") 

def copy_to_clipboard():
    password = result_entry.get()
    
    if password == "":  
        messagebox.showwarning(
            "Warning", 
            "There is no password to copy. please generate a password first." 
        )
        return 
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    messagebox.showinfo(
        "copied",
        "Password copied to clipboard." 
    )

window = tk.Tk()

window.title("Secure Password Generator") 

window.geometry("500x400")

title_label = tk.Label( 
    window,
    text="Secure Password Generator",
    font=("Arial", 16, "bold")   
) 

title_label.pack(pady=15) 

length_label = tk.Label(
    window,
    text="password Length:"
)
length_label.pack()

length_entry = tk.Entry(
    window,
    width=20
)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar() 

uppercase_check = tk.Checkbutton(
    window,
    text="Uppercase Letters",
    variable=uppercase_var 
)
uppercase_check.pack(anchor="w", padx=150) 

lowercase_check = tk.Checkbutton(
    window,
    text="Lowercase Letters",
    variable=lowercase_var 
)
lowercase_check.pack(anchor="w", padx=150) 

numbers_check = tk.Checkbutton(
    window,
    text="Numbers",
    variable=numbers_var
)
numbers_check.pack(anchor="w", padx=150) 

symbols_check = tk.Checkbutton(
    window,
    text="Symbols",
    variable=symbols_var
)
symbols_check.pack(anchor="w", padx=150) 

generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate
)
generate_button.pack(pady=20) 

copy_button = tk.Button(
    window,
    text="Copy to Clipboard",
    command=copy_to_clipboard  
)

copy_button.pack(pady=10) 

result_label = tk.Label(
    window,
    text="Generated Password:",
    font=("Arial", 12, "bold") 
)
result_label.pack() 

result_entry = tk.Entry( 
    window,
    width=30, 
    font=("Consolas", 12) 
)
result_entry.pack(pady=10) 
result_entry.config(state="readonly") 

window.mainloop() 