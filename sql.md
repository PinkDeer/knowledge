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
