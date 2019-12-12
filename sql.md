### sql

#### select

Выборка всех записей из таблицы
```
SELECT * FROM tableName
```
Упорядочить или выбрать определённые столбцы
```
SELECT column2, column1, column4 FROM tableName
```
Получить только уникальные строки (вместо __DISTINICT__ по умолчанию принимается __ALL__ )
```
SELECT DISTINICT column2, column1 FROM tableName
```
Сортировака по указанным полям
```
ORDER BY
```