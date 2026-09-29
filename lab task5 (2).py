import tkinter as tk

def calculate():
    a = float(num1.get())
    b = float(num2.get())
    op = operator.get()

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    elif op == "/":
        answer = a / b

    result.config(text="Result: " + str(answer))

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number").pack()
num1 = tk.Entry(root)
num1.pack()

tk.Label(root, text="Second Number").pack()
num2 = tk.Entry(root)
num2.pack()

operator = tk.StringVar()
operator.set("+")

tk.OptionMenu(root, operator, "+", "-", "*", "/").pack()

tk.Button(root, text="Calculate", command=calculate).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()