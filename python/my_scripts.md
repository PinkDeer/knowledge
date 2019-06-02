Простой калькулятор
```
print('''Простой калькутор. Выполняет операции сложения, вычитания, умножения и деления.
Для справки введите команлу \"help\", для выхода \"exit\".
''')

import calc

while True:
    x = input("Введите число ")
    if x.isalpha() == True:
        print("Некорректное значение")
        continue
    # else:
    elif x.isdigit() == True:
        x = float(x)

    y = input("Введите второе число ")
    if y.isalpha() == True:
        print("Некорректное значение")
        continue
    # else:
    elif y.isdigit() == True:
        y = float(y)

    # s.isalpha() – проверяет, состоит ли строка только из букв
    # s.isdigit() – проверяет, состоит ли строка только из чисел

    operation = input("Какую операцию выполнить? ")
    if operation == "+":
        print(calc.sum(x,y))
    elif operation == "-":
        print(calc.subtraction(x,y))
    elif operation == "*":
        print(calc.multiplication(x,y))
    elif operation == "/":
        if y == 0:
            print("Делить на ноль нельзя")
            continue
        print(calc.division(x,y))
    elif operation == "help":
        calc.helpme()
        continue
    elif operation == "exit":
        break
    else:
        print("Некорректное значение")
        continue

```
calc.py
```
def helpme():
    print('''Для сложения чисел введите символ \"+\"
Для вычитания чисел введите символ \"-\"
Для умножения чисел введите символ \"*\"
Для деления чисел введите символ \"/\"
''')

def sum(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

```

ver 2
```
print('Для спрвки введите "help", для выхода "exit".')

def helpme():
    print("""

Справка
""")

while True:

    while True:
        x = input('Введите первое число: ')
        x = x.lower()
        if x == 'help':
            helpme()
            continue
        elif x == 'exit':
            break
        elif x.replace('.','',1).isdigit():
            x = float(x)
            break
        else:
            print('Некорректное значение')
            continue

    while True:
        y = input('Введите второе число: ')
        if y == 'help':
            helpme()
            continue
        elif y == 'exit':
            raise SystemExit
        elif y.replace('.','',1).isdigit():
            y = float(y)
            break
        else:
            print('Некорректное значение')
            continue
    while True:

        var = input('Какую операцию выполнить? (+, -, *, /) ')
        var = var.lower()
        if var == '+':
            print(x+y)
            break
        elif var == '-':
            print(x-y)
            break
        elif var == '*':
            print(x*y)
            break
        elif var == '/':
            (x/y)
            break
        elif var == 'help':
            helpme()
            continue
        elif var == 'exit':
            raise SystemExit
        else:
            print('Некорректное значение')
```
