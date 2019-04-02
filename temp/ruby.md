[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Git](/git.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## Ruby

* [Основы](#основы)

[Apps](https://github.com/PinkDeer/ruby)

#### Основы

##### Переменная

В языке Ruby можно создавать переменные — имена, ссылающиеся на значения. Объявлять переменные заранее в Ruby не обязательно; они автоматически создаются в момент присваивания. Присваивание выполняется оператором «=» (один знак равенства).
Имя переменной — это просто любая последовательность латинских букв и цифр, но первый символ должен быть буквой в нижнем регистре. Слова разделять символом подчеркивания.

##### Aнализ объектов

Метод inspect поддерживается всеми объектами Ruby. Он преобразует объект в строковое представление, удобное для отладки.

```
puts variable.inspect
```
или сокращення запись метода inspect
```
p variable
```
.methods - какие методы можно использовать для объекта
.class - класс объекта

##### Служебные последовательности в строках

Символ косой черты (\) и следующий за ним символ n образует служебную последовательность — часть строки, представляющую символы, которые не имеют обычного представления в исходном кодe.
```
"Jay\n"
```
\n - new line (line feed(lf)
\t - табуляция, выравнивание
\r - return (carriage return(cr)), вовращает курсов к началу строки (возврат каретки)ляция
\" - двойные кавычки
\' - одинарные кавычки
\\ - обратная косая черта

Обратная косая черта — это символ экранирования (escape character). Другими словами, если в строке стоит обратная черта и другой символ [которые образуют так называемую "escape-последовательность"], то они оба иногда трансформируются в один новый символ. Но две вещи, которые обратная черта всё-таки экранирует, это апостроф и сама обратная черта. (Это работает в одинарных кавычках).
```
'\'\text\'' -> 'text'
```

##### Условные команды
```
== - равно
!= - не равно
>= - больше или равно
<= - меньше или равно
> - больше
< - меньше
```
В Ruby поддерживается оператор логического отрицания «!», который превращает значение true в false (или наоборот).
```
if ! true
	puts "I won't be printed!"
end
```
```
if ! false
	puts "I will!"
end
```
Также существуетключевое слово not, которое лучше читается, но делает практически то же самое.
```
if not true
	puts "I won't be printed!"
end
```
```
if not false
	puts "I will!"
end
```
Если вам нужно проверить, что истинны оба условия, используйте оператор «&&» («И»).
```
if true && true
	puts "I'll be printed!"
end
```
```
if true && false
	puts "I won't!"
end
```
Если вы хотите проверить, что истинно хотя бы одно из двух условий, используйте оператор «||» («ИЛИ»).
```
if false || true
	puts "I'll be printed!"
end
```
```
if false || false
	puts "I won't!"
end
```
Код команды if выполняется только в том случае, если условие истинно. С другой стороны, код команды unless выполняется только в том случае, если условние ложно.
Следующий код не выполнится:
```
unless true
	puts "I won't be printed!"
end
```
А этот сработает:
```
unless false
	puts "I will!"
end
```
##### Циклы

Цикл while состоит из ключевого слова while, логического выражения, выполняемого кода и ключевого слова end. Код в теле цикла продолжает выполняться, пока условие остается истинным.
```
number = 1
	while number <= 5
	puts number
	number += 1
end
```
Цикл until повторяется до того момента, когда условие станет истинным (то есть цикл продолжает выполняться, пока его условие остается ложным).
```
number = 1
	until number > 5
	puts number
	number += 1
end
```
##### Методы

Чтобы при вызове вашего метода передавались аргументы, в определение метода необходимо добавить параметры. Каждый аргумент в вызове метода сохраняется в одном из параметров внутри метода.
Тело метода состоит из одной или нескольких команд Ruby, которые выполняются при вызове метода.
```
def print_sum(arg1, arg2)
	print arg1 + arg2
end
```
Имена методов следует записывать в «змеином» стиле: одно или несколь­ко слов в нижнем регистре, разделен­ных подчеркиваниями (как в именах переменных).
Также имя метода может завершаться вопросительным (?) или восклицательным знаком (!). Такие суффиксы не имеют
специального смысла в языке Ruby, но, по общепринятым соглашениям, именам, возвращающим логическое значение (true/false), присваиваются имена, завершающиеся знаком «?», методам с возможными неожиданными побочными эффектами присваиваются имена, завершающиеся знаком «!».
Имя метода может завершаться знаком равенства (=). Методы, имена которых завершаются этим символом, используются для назначения атрибутов. В языке Ruby этот суффикс имеет специальный смысл, поэтому не применяйте его в обычных методах — или вы увидите, что ваш метод ведет себя странно.

###### Необязательные параметры

В обяъвлени метода можно задать значени по умолчанию для необязательного парметра.
```
def order_soda(flavor, size = "medium", quantity = 1)
	if quantity == 1
		plural = "soda"
	else
		plural = "sodas"
		end
		puts "#{quantity} #{size} #{flavor} #{plural}, coming right up!"
end
```
Если потребуется заменить значение по умолчанию, просто передайте аргумент с нужным значением. А если устраивает значение по умолчанию, аргумент просто не указывается.
При использовании необязательных параметров необходимо помнить об одном правиле: они должны следовать после всех остальных параметров. Если обязательный параметр следует в списке за необязательным, то опустить необязательный параметр не удастся.
Вызов:
```
order_soda "orange"
order_soda "lemon-lime", "small", 2
order_soda "grape", "large"
```
Получаем:
```
1 medium orange soda, coming right up!
2 small lemon-lime sodas, coming right up!
1 large grape soda, coming right up!
```

###### Возвращаемые значечния

Как и в большинстве языков, методы Ruby имеют возвращае­ мое значение, которое передается вызвавшему их коду. Метод Ruby возвращает значение вызывающей стороне с помощью ключевого слова *return*.
Ключевое слово *return* в этом методе не обязательно. Значение последнего выражения, вычисленного в методе, автоматически становится возвращаемым значением этого
метода.

**Раннее возвращение из метода.**

Существуют обстоятельства, в которых ключевое слово *return* может оказаться полезным.
Ключевое слово *return* приводит к немедленному выходу из метода без выполнения оставшегося кода. Это бывает полезно в ситуациях, когда выполнение этого кода будет бессмысленно или даже вредно.
Пример:
```
def mileage(miles_driven, gas_used)
	if gas_used == 0
			return 0.0
	end
		miles_driven / gas_used
end

trip_mileage = mileage(400, 12)
puts "You got #{trip_mileage} MPG on this trip."
lifetime_mileage = mileage(11432, 366)
puts "This car averages #{lifetime_mileage} MPG."

```

###### irb

Загрузка файла в irb
```
irb I- .
```
-I — параметр командной строки, который добавляется в команду для изменения режима ее выполнения. В данном случае -I изменяет набор каталогов, в которых Ruby ищет загружаемые файлы. Точка (.) обозначает текущий каталог.

Открытие файла в в irb
```
require "file_name"
```
Если будет выведен результат true, значит, файл загрузился успешно.
Можно обращаться к методам из файла.



### _Черновик_


##### Методы


.to_i - игнорирует всё, начиная с первой конструкции, которая не распознана как число, и далее до конца строки.
```
puts '5 - это моё любимое число!'.to_i
```
```
5
```
Если строка начинается с буквы, то все игнортруется и выводится ноль
```
puts 'Кто вас спрашивал о 5 или о чём-нибудь подобном?'.to_i
```
```
0
```

#### Числа

При выполнении арифметические действия с целыми числами, вы получаете целочисленные ответы.

```
puts 9/2
```
Результат
```
4
```
#### Арифмитические методы


\+ - соржение  
\- - вычитание  
\* - умножение  
/ - деление  
** - возведение в степень  
% - деление по модулю  
```
puts 5**2
puts 5**0.5
puts 7/3
puts 7%3
puts 365%7
```
```
25
2.23606797749979
2
1
1
```
abs - берёт абсолютное значение указанного числа:  
```
puts((5-2).abs)
puts((2-5).abs)
```
```
3
3
```
rand - генератор случайных чисел  
Если вы вызовете rand как есть (без аргументов), вы получите дробное число, большее или равное 0.0 и меньшее 1.0. Если вы дадите методу rand целое (например, 5), он вернёт вам целое число, большее или равное 0 и меньшее, чем 5 (то есть одно из пяти возможных чисел, от 0 до 4).
```
puts rand
puts rand
puts rand
puts(rand(100))
puts(rand(100))
puts(rand(100))
puts(rand(1))
puts(rand(1))
puts(rand(1))
puts(rand(99999999999999999999999999999999999999999999999999999999999))
puts('Синоптик сказал, что с вероятностью в '+rand(101).to_s+'% пойдёт дождь,')
puts('но никогда не стоит доверять синоптикам.')
```
```
0.053950924931684
0.975039266747952
0.436084118016833
63
40
38
0
0
0
54350491927962189206794015651522429182285732200948685516886
Синоптик сказал, что с вероятностью в 22% пойдёт дождь,
но никогда не стоит доверять синоптикам.
```

Обратите внимание, что я использовал rand(101), чтобы получить числа от 0 до 100, и что rand(1) всегда возвращает 0.

srand - возвращаtn те же самые случайные числа в той же последовательности при двух разных запусках вашей программы
```
srand 1776
puts(rand(100))
puts(rand(100))
puts(rand(100))
puts(rand(100))
puts(rand(100))
puts ''
srand 1776
puts(rand(100))
puts(rand(100))
puts(rand(100))
puts(rand(100))
puts(rand(100))
```
```
24
35
36
58
70

24
35
36
58
70
```
Если вы снова хотите получать различные числа (также, как происходит, если вы не применяли до этого srand), то просто вызовите srand 0.

Объект Math

```
puts(Math::PI)
puts(Math::E)
puts(Math.cos(Math::PI/3))
puts(Math.tan(Math::PI/4))
puts(Math.log(Math::E**2))
puts((1 + Math.sqrt(5))/2)
```
```
3.14159265358979
2.71828182845905
0.5
1.0
2.0
1.61803398874989
```


#### Строковые методы

.reverse - не переворачивает значение исходной строки, он просто создаёт её новую перевёрнутую копию  
.length - количество символов в строке включая пробелы  
.upcase - изменяет каждую строчную букву на заглавную  
.downcase - изменяет каждую заглавную букву на строчную  
.swapcase - переключает регистр каждой буквы в строке  
.capitalize - переводит первый символ в заглавную (если это буква)  
.center - центрирует строчку  
```
lineWidth = 50
puts(  'Вот вам юная мисс из России:'.center(lineWidth))
```
.ljust - выровнять влево (left justify)
.rjust - выровнять вправо (left right jisttify)
```
lineWidth = 40
str = '--> текст <--'
puts str.ljust  lineWidth
puts str.center lineWidth
puts str.rjust  lineWidth
puts str.ljust (lineWidth/2) + str.rjust (lineWidth/2)
```

#### Операторы

puts (put string) - выводит на экран всё, что следут за ним. Прежде, чем метод puts пытается вывести объект, он использует to_s , чтобы получить строковую версию этого объекта
print
gets
gets.chomp - метод chomp убирает все символы Enter d в конце строки
strip - удаляет whitespice символы
exit - прервать програму
&& -
break - выйти из блока (итератора) и продолжать выполнять программу дальше)


#### Присваивание переменной

a = 10

#### Команды
irb - интерпретатор ruby

#### Типы данных

1.class - определить тип данных

string - "аа" "2"
fixnum 2 22
float 3.14
array [...]
hash  {}

Преобразование:
.to_s
.to_i
.to_f

Интерполяция:

x = 2
puts "x = #{x}" (только двойные кавычки)

str.chomp! - ! указывает применить операцию chomp к  str.

x.methods - список операций

times

10.times {puts ""}

or

10.times do
	puts
end

another

10.times {|i| puts i}

or

10.times do |i|
	puts i
end





Руби возвращает НОЛЬ, когда не знает что возвращать

делигаты, люямба выражения - указатель на функцию

@a - глобальная переменная (везде), переопределяется
: - символы в памяти разполагаются в одноме месте


#### Массивы

arr = [] инициализация пустого массива
arr = Array.new инициализация пустого массива
arr = ["Text", 33] инициализация массива
arr << "Cat" добавить в массив
arr = %w[Text 33 Cat] инциализация с пробелами между элементами
arr = [:left, :richt] инциализация c символами (т.е. любые объекты)
arr [индекс] - доступ к элементам массива (индекс от 0 до ...)

arr.delete_at 0 (0 - индекс)
arr.dekete "aa" ("aa" - объекат)

[["mike", 56],["alex", 72]] - двумерный массив


Вывод массиса в порядковым номером

arr = %w[make jr hank]

arr.each_with_index do |name, index|
  puts "#{index + 1}. #{name}"
end


or

x = 0
arr.each do |item|
  x = x + 1
  puts "#{x} #{item}"
end



arr ["text"] = ["text2","text3"] = заменить значение

##### Обменять значение двух переменных:

a, b = b, a (objects)
or (integer)
a = a + b
b = a - b
a = a - b

#### Хеш

hh = {}
hh = {'mike'=>'35373',
			'jessie'=>'31380'} - инициалазация хеша.
hh = Hash.new - инициалазация хеша.

hh ['alex'] = 65 - добавить в хеш
hh.store('mike', 65) - добавить в хеш
hh ['alex'] - доступ/обращение к элементу хэша по ключу

hh.keys -> 35373 31380 (выводит ключи, массив ключей(аналогично .value, из каждого значения отдельыне мыссив))

puts hh - вывести на экран
puts hh.inspect - вывести на экран (другой формат вывода)

так же можно вывести через each

.each do |key, value|
	puts "#{key}, #{value}"
end

.each_key do |key|

.each_value do |value|


вывести ключи/значнея

puts hh.keys
puts hh.keys.inspect

puts hh.values
puts hh.values.inspect

вывести значение

hh = {}
hh.each.keys do |key|
	value = hh[key]
end


проверить ключ в хеше

1)	if hh.has_key? 'mike'
			puts 'В хеше есть слово "mike"'
		end
2)  if hh['mike']

		end

hh.clear - очистка хеша

hh.delete key - удалить из кеша





puts "ok" if true - будет исполнено

#### Записать в файл

ruby app1.rb > file.text - перезаписать
ruby app1.rb >> file.text - дописать в конец

#### Атрибуты

attr_reader - для чтения
attr_accessor - для чтения и для записи
attr_writer - только запись