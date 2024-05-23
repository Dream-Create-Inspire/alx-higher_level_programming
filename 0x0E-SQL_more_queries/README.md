#0x0E. SQL - More queries

##Learning Objectives

How to create a new MySQL user
To create a new MySQL user, you can use the CREATE USER statement followed by the GRANT statement to assign privileges. Here is an example:

sql
Copy code
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
This creates a new user newuser with the password password and grants them all privileges.

How to manage privileges for a user to a database or table
Managing privileges involves using the GRANT and REVOKE statements. Here is an example of granting privileges:

sql
Copy code
GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'username'@'host';
And here is an example of revoking privileges:

sql
Copy code
REVOKE INSERT ON database_name.table_name FROM 'username'@'host';
Always use FLUSH PRIVILEGES to ensure that the changes take effect immediately.

What’s a PRIMARY KEY
A PRIMARY KEY is a field (or combination of fields) in a table that uniquely identifies each row. It ensures that no two rows can have the same primary key value, and it cannot contain NULL values.

sql
Copy code
CREATE TABLE example (
    id INT NOT NULL,
    name VARCHAR(100),
    PRIMARY KEY (id)
);
What’s a FOREIGN KEY
A FOREIGN KEY is a field (or combination of fields) that establishes a link between data in two tables. It enforces referential integrity by ensuring that the value in the foreign key field corresponds to a value in the primary key field of another table.

sql
Copy code
CREATE TABLE orders (
    order_id INT NOT NULL,
    customer_id INT,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
How to use NOT NULL and UNIQUE constraints
NOT NULL ensures that a column cannot have a NULL value.
UNIQUE ensures that all values in a column are distinct.
sql
Copy code
CREATE TABLE example (
    id INT NOT NULL,
    email VARCHAR(100) UNIQUE
);
How to retrieve data from multiple tables in one request
You can retrieve data from multiple tables using JOIN clauses. Here is an example using INNER JOIN:

sql
Copy code
SELECT orders.order_id, customers.name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
What are subqueries
A subquery is a query nested inside another query. It can be used in SELECT, INSERT, UPDATE, or DELETE statements.

sql
Copy code
SELECT name
FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE amount > 100);
What are JOIN and UNION
JOIN is used to combine rows from two or more tables based on a related column.
UNION is used to combine the results of two or more SELECT statements.
JOIN example:
sql
Copy code
SELECT orders.order_id, customers.name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
UNION example:
sql
Copy code
SELECT name FROM customers
UNION
SELECT name FROM suppliers;
Note that both SELECT statements in a UNION must have the same number of columns in the result sets with compatible data types.

Feel free to ask if you need more details on any of these topics!
