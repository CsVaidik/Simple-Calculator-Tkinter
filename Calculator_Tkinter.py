import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except SyntaxError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')
    except NameError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')
        

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="blue")



entry = tk.Entry(root, width=40, borderwidth=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

# Create and position the buttons
row = 1
c = 0
for button in buttons:
    btn = tk.Button(root, text=button,bg="black",fg="white", padx=20, pady=10,
                    command=lambda btn=button: button_click(btn))
    btn.grid(row=row, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        row += 1

# Create the Clear button
clear_btn = tk.Button(root, text="C",bg="black",fg="white", padx=20, pady=10, command=button_clear)
clear_btn.grid(row=row, column=c, padx=5, pady=5)

# Create the Equal button
equal_btn = tk.Button(root, text="=",bg="black",fg="white", padx=20, pady=10, command=button_equal)
equal_btn.grid(row=row+1, column=c, padx=5, pady=5)


root.mainloop()
