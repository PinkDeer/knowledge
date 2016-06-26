Создание новой база данных
Создание новой таблица
первое поле обычно id, data type Integer
установить primary key and autoincrement


SELECT * FROM table_name - вепнуть всю таблицу


добавить в таблицу
INSERT INTO table_name (column1, column2, column3) VALUES (1, значенин, значение)
если в первом поле автоинеремент, то поле и значение указвать не надо.


работы с базой в консоли:

$ sqlite3 databases_name

.table - список таблиц
.exit - выход

select * from table_name - для завершения запроса необходимо в ставить ;

.mode column - визуальная разбивка на стобцы

.headers on - выводит названия столбцов


типы данных sql http://sql-language.ru/sqldatetype.html

datetime - можно использовать date_stamp


CREATE TABLE Users (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    username  TEXT,
    phone     VARCHAR,
    datestamp TEXT,
    barber    TEXT,
    color     TEXT
);

or создать таблицу если не создана

CREATE TABLE IF NOT EXISTS Users(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    username  TEXT,
    phone     VARCHAR,
    datastamp TEXT,
    barber    TEXT,
    color     TEXT
);

удалить таблицу
drop table table_name
