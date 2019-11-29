## C#


### Полезная информация

C# является регистрозависимым языком.

Все ключевые слова в C# вводятся в нижнем регистре, а названия пространсва имён, типов, членов - начинаются с заглавной буквы и имеют залавную букву в любых содержащихся внутри словах.


### Типы данных

[Официальная документация](https://docs.microsoft.com/ru-ru/dotnet/csharp/language-reference/keywords/built-in-types-table)  
[Консольное приложение](https://github.com/PinkDeer/ConsoleApps/blob/master/DataTypes/Program.cs)


### Переменная

Обявление
```
тип_данных имя_перменной;
```
Инициализация
```
имя_переменной = значение;
```
В одну строку
```
тип_данных имя_перменной = значение;
```
Объявление нескольких переменных одного типа
```
тип_данных имя_перменной_1, имя_перменной_1;
```
char и string
```
char = '';
string = "";
```
[Примеры](https://github.com/PinkDeer/ConsoleApps/blob/master/variables/Program.cs)

### Ввод данных в консоль

Запись в переменную
```
string name = Console.ReadLine();
```
Вывод
```
Console.WriteLine("Hello, " + name + "!");
Console.WriteLine($"Hello, {name}!");
```
[Примеры](https://github.com/PinkDeer/ConsoleApps/blob/master/InputToTheConsole/Program.cs)


### Конвертация

[Класс Convert (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/api/system.convert?view=netframework-4.8)  
[Пример конвертации в string в int](https://github.com/PinkDeer/ConsoleApps/blob/master/Conversion/Program.cs)  
[Пример конвертация дроби с точкой](https://github.com/PinkDeer/ConsoleApps/blob/master/FractionConversion/Program.cs)  
[Метод Parse (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/api/system.int32.parse?view=netframework-4.8#System_Int32_Parse_System_String_System_Globalization_NumberStyles_)  
[Метод TryParse (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/api/system.int32.tryparse?view=netframework-4.8)  
[Примеры Parse и TryParse](https://github.com/PinkDeer/ConsoleApps/blob/master/ParseTryparse/Program.cs)

### Арифметические операторы

Бинарные арифметические операции: сложение(+), вычитание(-), умножение(*), деление(/), получение остатка от целочисленного деления двух чисел(%).

[Арифметические операции (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/csharp/language-reference/operators/arithmetic-operators)  
[Статья на metanit.com](https://metanit.com/sharp/tutorial/2.3.php)  
[Примеры операций](https://github.com/PinkDeer/ConsoleApps/blob/master/ArithmeticOperations/Program.cs)|[Примеры инкремента и декремента](https://github.com/PinkDeer/ConsoleApps/blob/master/Increment%2CDecrement/Program.cs)  

### Условные варажения

[Операторы сравнения (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/csharp/language-reference/operators/comparison-operators)
[Логические операторы](https://docs.microsoft.com/ru-ru/dotnet/csharp/language-reference/operators/boolean-logical-operators)  
[Статья на metanit.com](https://metanit.com/sharp/tutorial/2.24.php)
