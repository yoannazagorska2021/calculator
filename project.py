import tkinter as tk


def get_operands(stack):
    """ Pop two operands from the stack and return them. """
    return stack.pop(), stack.pop()


def op_plus(stack):
    x, y = get_operands(stack)
    stack.append(x + y)


def op_minus(stack):
    x, y = get_operands(stack)
    stack.append(y - x)


def op_multiply(stack):
    x, y = get_operands(stack)
    stack.append(x * y)


def op_divide(stack):
    x, y = get_operands(stack)
    stack.append(y / x)


def op_power(stack):
    x, y = get_operands(stack)
    stack.append(y ** x)


def evaluate_expression():
    stack = []
    tokens = display.get().strip().split()
    for token in tokens:
        if token in operators:
            operators[token](stack)
        else:
            stack.append(float(token))
    result = stack[0]
    if result.is_integer():
        display.set(str(int(result)))
    else:
        display.set(str(result))


def button_click(button_text):
    current_expression = display.get()

    if button_text == "C":
        display.set("")
    elif button_text == "Enter":
        evaluate_expression()
    elif button_text == "Del":
        display.set(current_expression[:-1])  # Remove the last character
    else:
        display.set(current_expression + " " + button_text)


def on_enter_key(event):
    evaluate_expression()


root = tk.Tk()
root.title("RPN Calculator")
root.configure(bg="#f0f0f0")  # Set background color to gray

display = tk.StringVar()
display_entry = tk.Entry(root,
                         textvariable=display,
                         justify="right",
                         font=("Arial", 24),
                         bd=0,
                         relief=tk.FLAT)
display_entry.grid(row=0,
                   column=0,
                   columnspan=4,
                   padx=10,
                   pady=10,
                   ipady=15)

buttons = [
    ("C", 1, 0, "#ACACAC"),
    ("Del", 1, 1, "#ACACAC"),
    ("/", 1, 2, "#FF9500"),
    ("*", 1, 3, "#FF9500"),
    ("7", 2, 0, "#E4E4E4"),
    ("8", 2, 1, "#E4E4E4"),
    ("9", 2, 2, "#E4E4E4"),
    ("-", 2, 3, "#FF9500"),
    ("4", 3, 0, "#E4E4E4"),
    ("5", 3, 1, "#E4E4E4"),
    ("6", 3, 2, "#E4E4E4"),
    ("+", 3, 3, "#FF9500"),
    ("1", 4, 0, "#E4E4E4"),
    ("2", 4, 1, "#E4E4E4"),
    ("3", 4, 2, "#E4E4E4"),
    ("Enter", 4, 3, "#FF9500"),
    ("0", 5, 0, "#E4E4E4"),
    (".", 5, 1, "#E4E4E4"),
]

for button_text, row, column, color in buttons:
    button = tk.Button(root,
                       text=button_text,
                       width=6,
                       height=3,
                       bg=color,
                       fg="#000000",
                       font=("Arial", 16),
                       bd=0,
                       relief=tk.RAISED)
    button.grid(row=row,
                column=column,
                padx=5,
                pady=5,
                sticky="nsew")

    button.bind("<Button-1>", lambda event, text=button_text: button_click(text))

operators = {
    "+": op_plus,
    "-": op_minus,
    "*": op_multiply,
    "/": op_divide,
    "**": op_power
}

display_entry.focus_set()  # Set focus on the display_entry for immediate input

root.bind("<Return>", on_enter_key)  # Bind the Enter key to the function

root.mainloop()
