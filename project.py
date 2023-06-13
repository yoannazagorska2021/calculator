import tkinter as tk  # Импортиране на модула tkinter и задаване на псевдоним tk

def get_operands(stack):
    """ Pop two operands from the stack and return them. """
    return stack.pop(), stack.pop()  # Изваждане на два операнда от стека и връщане на тях


def op_plus(stack):
    x, y = get_operands(stack)  # Извличане на операндите от стека
    stack.append(x + y)  # Добавяне на сбора на операндите в стека


def op_minus(stack):
    x, y = get_operands(stack)  # Извличане на операндите от стека
    stack.append(y - x)  # Добавяне на разликата на операндите в стека


def op_multiply(stack):
    x, y = get_operands(stack)  # Извличане на операндите от стека
    stack.append(x * y)  # Добавяне на произведението на операндите в стека


def op_divide(stack):
    x, y = get_operands(stack)  # Извличане на операндите от стека
    stack.append(y / x)  # Добавяне на частното на операндите в стека


def op_power(stack):
    x, y = get_operands(stack)  # Извличане на операндите от стека
    stack.append(y ** x)  # Добавяне на степента на операндите в стека


def evaluate_expression():
    stack = []  # Създаване на празен стек за операндите
    tokens = display.get().strip().split()  # Извличане на входните токени от текстовото поле и разделяне на токените
    for token in tokens:
        if token in operators:  # Ако текущият токен е оператор
            operators[token](stack)  # Извикване на съответната функция за операцията
        else:  # Ако текущият токен е операнд
            stack.append(float(token))  # Преобразуване на токена в число и добавяне на операнда в стека
    result = stack[0]  # Резултатът е стойността на първия елемент в стека
    if result.is_integer():  # Ако резултатът е цяло число
        display.set(str(int(result)))  # Задаване на цялата част на резултата като нова стойност за изобразяване
    else:  # Ако резултатът е дробно число
        display.set(str(result))  # Задаване на резултата като нова стойност за изобразяване


def button_click(button_text):
    current_expression = display.get()  # Получаване на текущия израз от текстовото поле

    if button_text == "C":  # Ако бутона е "C"
        display.set("")  # Изчистване на текстовото поле
    elif button_text == "Enter":  # Ако бутона е "Enter"
        evaluate_expression()  # Изчисляване на израза
    elif button_text == "Del":  # Ако бутона е "Del"
        display.set(current_expression[:-1])  # Премахване на последния символ от текущия израз
    else:  # Ако бутона е цифра или оператор
        display.set(current_expression + " " + button_text)  # Добавяне на цифрата или оператора към текущия израз


def on_enter_key(event):
    evaluate_expression()  # Изчисляване на израза


root = tk.Tk()  # Създаване на главното прозорец на приложението
root.title("RPN Calculator")  # Заглавие на прозореца
root.configure(bg="#f0f0f0")  # Задаване на фонов цвят на прозореца

display = tk.StringVar()  # Създаване на променлива за изобразяване на текста
display_entry = tk.Entry(root,
                         textvariable=display,
                         justify="right",
                         font=("Arial", 24),
                         bd=0,
                         relief=tk.FLAT)  # Създаване на текстово поле за въвеждане
display_entry.grid(row=0,
                   column=0,
                   columnspan=4,
                   padx=10,
                   pady=10,
                   ipady=15)  # Позициониране на текстовото поле в прозореца

buttons = [
    ("C", 1, 0, "#ACACAC"),  # Бутон "C"
    ("Del", 1, 1, "#ACACAC"),  # Бутон "Del"
    ("/", 1, 2, "#FF9500"),  # Бутон "/"
    ("*", 1, 3, "#FF9500"),  # Бутон "*"
    ("7", 2, 0, "#E4E4E4"),  # Бутон "7"
    ("8", 2, 1, "#E4E4E4"),  # Бутон "8"
    ("9", 2, 2, "#E4E4E4"),  # Бутон "9"
    ("-", 2, 3, "#FF9500"),  # Бутон "-"
    ("4", 3, 0, "#E4E4E4"),  # Бутон "4"
    ("5", 3, 1, "#E4E4E4"),  # Бутон "5"
    ("6", 3, 2, "#E4E4E4"),  # Бутон "6"
    ("+", 3, 3, "#FF9500"),  # Бутон "+"
    ("1", 4, 0, "#E4E4E4"),  # Бутон "1"
    ("2", 4, 1, "#E4E4E4"),  # Бутон "2"
    ("3", 4, 2, "#E4E4E4"),  # Бутон "3"
    ("Enter", 4, 3, "#FF9500"),  # Бутон "Enter"
    ("0", 5, 0, "#E4E4E4"),  # Бутон "0"
    (".", 5, 1, "#E4E4E4"),  # Бутон "."
    (" ", 5, 2, "#E4E4E4"),  # space button
]

for button_text, row, column, color in buttons:  # За всеки елемент в списъка buttons
    button = tk.Button(root,  # Създаване на бутон
                       text=button_text,  # Задаване на текста на бутона
                       width=6,  # Задаване на ширината на бутона
                       height=3,  # Задаване на височината на бутона
                       bg=color,  # Задаване на цвета на фона на бутона
                       fg="#000000",  # Задаване на цвета на шрифта на бутона
                       font=("Arial", 16),  # Задаване на шрифта на бутона
                       bd=0,  # Задаване на дебелината на границата на бутона
                       relief=tk.RAISED)   # Създаване на бутон със зададени параметри
    button.grid(row=row, # Позициониране на бутона в прозореца (на определен ред и колона с падинг и лепене)
                column=column,  # Задаване на колоната, на която ще се позиционира бутона
                padx=5,  # Задаване на отстояние по хоризонтала около бутона
                pady=5,  # Задаване на отстояние по вертикала около бутона
                sticky="nsew")  # Задаване на начина на лепене на бутона спрямо съседните елементи

    button.bind("<Button-1>", lambda event, text=button_text: button_click(text))  # Свързване на бутона с функцията при щракване

operators = {
    "+": op_plus,  # Оператор "+"
    "-": op_minus,  # Оператор "-"
    "*": op_multiply,  # Оператор "*"
    "/": op_divide,  # Оператор "/"
    "**": op_power  # Оператор "**"
}

display_entry.focus_set()  # Фокусиране на текстовото поле за незабавен вход

root.bind("<Return>", on_enter_key)  # Свързване на клавиш "Enter" с функцията

root.mainloop()  # Стартиране на главния цикъл на приложението
