# SQL - structured query language — «язык структурированных запросов»
SQL предназначен для сохранения, манипуляции и получения данных, которые хранятся в реляционной базе данных

## SQL Команды
Стандартные SQL команды для взаимодействия с реляционными БД:
- CREATE - Создаёт новую таблицу, вид таблицы или другой объект в БД.
- SELECT - Получает определённые данные из одной или нескольких таблиц.
- INSERT - Создаёт запись
- UPDATE - Изменяет записи
- DELETE - Удаляет записи
- DROP - Удаляет указанную таблицу, вид таблицы или другой объект БД.

## Синтаксис команд
### CREATE
```sql
CREATE TABLE имя_таблицы(
колонка1 тип_данных,
колонка2 тип_данных,
колонка3 тип_данных,
...
PRIMARY KEY( одни или несколько колонок )
);
```

### SELECT
```sql
SELECT колонка1, колонка2 ...
FROM   имя_таблицы;
```
```sql
Для получения всех данных:

SELECT *
FROM   имя_таблицы;
```
#### Условие WHERE
```sql
SELECT колонка1, колонка2 ...
FROM   имя_таблицы
WHERE  условие;
```

#### Условие AND/OR
```sql
SELECT колонка1, колонка2 ...
FROM    имя_таблицы
WHERE  условие-1 {AND|OR} условие-2;
```
### INSERT
```sql
INSERT INTO имя_таблицы (колонка1, колонка2 ...)
VALUES ( значение1, значение2 ...);
```
### UPDATE
```sql
UPDATE table_name
SET колонка1 = значение1, колонка2 = значение2 ...
[ WHERE условие ];
```
### DELETE
```sql
DELETE FROM имя_таблицы
WHERE  {условие};
```
### DROP
```sql
DROP TABLE имя_таблицы;
```