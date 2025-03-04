import tkinter as tk
import math

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "⌫":
        entry_var.set(entry_var.get()[:-1])
    elif button_text == "=":
        try:
            expression = entry_var.get()
            expression = expression.replace("^", "**").replace("√", "math.sqrt")
            expression = expression.replace("π", str(math.pi)).replace("e", str(math.e))
            expression = expression.replace("log", "math.log10").replace("ln", "math.log")
            expression = expression.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
            expression = expression.replace("asin", "math.asin").replace("acos", "math.acos").replace("atan", "math.atan")

            if "!" in expression:  
                expression = expression.replace("!", "")
                result = math.factorial(int(entry_var.get().replace("!", "")))
            else:
                result = eval(expression, {"math": math, "__builtins__": None})
            
            entry_var.set(str(result))
        except:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + button_text)

root = tk.Tk()
root.title("Calculadora Científica")
root.configure(bg="#14532D")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, bg="#86EFAC", fg="#000000")
entry.grid(row=0, column=0, columnspan=6)

buttons = [
    ("7", "8", "9", "/", "sin", "cos"),
    ("4", "5", "6", "*", "tan", "asin"),
    ("1", "2", "3", "-", "acos", "atan"),
    ("C", "0", "=", "+", "log", "ln"),
    ("(", ")", "^", "√", "π", "e"),
    ("%", ".", "00", "!", "⌫", "Exit")
]

button_bg = "#22C55E"
button_fg = "#FFFFFF"
button_active_bg = "#16A34A"

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        button = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2,
                           bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                           command=lambda ch=char: on_click(ch) if ch != "Exit" else root.quit())
        button.grid(row=r + 1, column=c)

root.mainloop()