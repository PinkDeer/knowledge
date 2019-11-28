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
[Пример](https://github.com/PinkDeer/ConsoleApps/blob/master/variables/Program.cs)

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
[Пример](https://github.com/PinkDeer/ConsoleApps/blob/master/InputToTheConsole/Program.cs)


### Конвертация

[Класс Convert (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/api/system.convert?view=netframework-4.8)  
[Пример конвертации в string в int](https://github.com/PinkDeer/ConsoleApps/blob/master/Conversion/Program.cs)  
[Пример конвертация дроби с точкой](https://github.com/PinkDeer/ConsoleApps/blob/master/FractionConversion/Program.cs)  
[Метод Parse (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/api/system.int32.parse?view=netframework-4.8#System_Int32_Parse_System_String_System_Globalization_NumberStyles_)  
[Метод TryParse (Официальная документация)](https://docs.microsoft.com/ru-ru/dotnet/api/system.int32.tryparse?view=netframework-4.8)  
[Пример Parse и TryParse](https://github.com/PinkDeer/ConsoleApps/blob/master/ParseTryparse/Program.cs)