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
