### sql

#### select

Выборка всех записей из таблицы
```
SELECT * FROM tableName
```
Упорядочить или выбрать опредеённые столбцы
```
SELECT column2, column1, column4 FROM tableName
```
Получить только уникальный строки (вместо __DISTINICT__ по умолчанию принимается __ALL__ )
```
SELECT DISTINICT column2, column1 FROM tableName
```