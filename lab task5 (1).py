import tkinter as tk

def greater():
    a = float(num1.get())
    b = float(num2.get())

    if a > b:
        result.config(text="Greater number: " + str(a))
    elif b > a:
        result.config(text="Greater number: " + str(b))
    else:
        result.config(text="Both numbers are equal")

root = tk.Tk()
root.title("Greater Number")

tk.Label(root, text="Enter first number").pack()
num1 = tk.Entry(root)
num1.pack()

tk.Label(root, text="Enter second number").pack()
num2 = tk.Entry(root)
num2.pack()

tk.Button(root, text="Find Greater", command=greater).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()