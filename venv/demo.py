1.Получает все столбцы и все записи из таблицы Customers.
SELECT * FROM Customers;
2.Получает только столбцы идентификатор, имя, адрес и все записи из таблицы Customers.
SELECT CustomerID,CustomerName,Address From Customers;
3.Получает все столбцы и все записи кто из Франции
SELECT Country FROM Customers;
4.Получите только имена клиентов из Лондона.
SELECT  CustomerName From Customers WHERE CITY = "London"