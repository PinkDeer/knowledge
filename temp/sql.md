[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Git](/git.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## SQL

* [Типпы данных](#Типпы-данных)
* [Команды](#Команды)
* [Консоль](#Консоль)
* [Полезное](#Полезное)

### Типы данных

[Типы данных sql](http://sql-language.ru/sqldatetype.html)  

[![up](/image/up.png)](#sql)  

### Команды

select * from table_name - вернуть всю таблицу
drop table table_name - удалить таблицу

[![up](/image/up.png)](#sql)

### Консоль

Сперва необходимо создать БД, далее войти в неё:
```
sqlite3 basename.sqlite
```
Пример создания таблицы
````
CREATE TABLE "Users" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "username" TEXT, "phone" TEXT, "datestamp" TEXT, "barber" TEXT, "color" TEXT)
```
Удобно использовать при инициализации приложения:
````
CREATE TABLE IF NOT EXISTS "Users" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "username" TEXT, "phone" TEXT, "datestamp" TEXT, "barber" TEXT, "color" TEXT)
```
Для завершения запроса необходимо в конце строчки ставить  символ";"  

Открыть таблицу в консоли
```
$ sqlite3 databases_name
```
Список таблиц
```
sqlite> .table
```
Визуальная разбивка на столбцы
```
sqlite> .mode column
```
Вывод названия столбцов
```
sqlite> .headers on
```
Выход из консоли
```
sqlite> .exit - выход
```
Удалить всё из таблицы:
```
delete from tablename
```
Информация о таблице
```
pragma table_info(tablename)
```

[![up](/image/up.png)](#sql)

### Полезное

#### Создание новой таблицы:

При созданий новой таблицы, первое поле обычно создается со следующмим параметрами:  
id, data type Integer, primary key and autoincrement

#### добавить в таблицу

insert into table_name (~~column1~~, column2, column3) VALUES (~~1~~, значение2, значение2)  
Если в первом поле автоинкремент, то поле первое поле и значение для него в запросе указвать не нужно.

#### Советы

datetime - зарезевированное имя, вместо него можно использовать _date_stamp_.

Если таблица не создана, то можно использовать команду:  
```
sqlite> create table if not exists table_name
```
[![up](/image/up.png)](#sql)
