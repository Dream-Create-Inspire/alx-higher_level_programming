#0x0D. SQL - Introduction

##Learning Objectives

General
What’s a database
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. Databases are managed by database management systems (DBMS) and are used to efficiently store, retrieve, and manage data.

What’s a relational database
A relational database is a type of database that stores data in tables (or relations), which are structured in rows and columns. Each table represents a different entity, and tables can be related to each other through keys. The relational model uses Structured Query Language (SQL) to interact with the data.

What does SQL stand for
SQL stands for Structured Query Language. It is a standard programming language used to manage and manipulate relational databases. SQL allows users to perform various operations like querying data, updating records, and managing database schema.

What’s MySQL
MySQL is an open-source relational database management system (RDBMS) based on SQL. It is widely used for web applications and is known for its reliability, performance, and ease of use. MySQL supports various SQL operations to manage and manipulate data in databases.

How to create a database in MySQL
To create a database in MySQL, you can use the CREATE DATABASE statement. Here’s an example:

sql
Copy code
CREATE DATABASE my_database;
This command creates a new database named my_database.

What does DDL and DML stand for
DDL stands for Data Definition Language. It includes SQL commands that define the structure of the database, such as CREATE, ALTER, and DROP statements.
DML stands for Data Manipulation Language. It includes SQL commands used to manipulate data within the database, such as INSERT, UPDATE, DELETE, and SELECT statements.
How to CREATE or ALTER a table
CREATE a table:

sql
Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
This command creates a table named users with three columns: id, name, and email.

ALTER a table:

sql
Copy code
ALTER TABLE users ADD COLUMN age INT;
This command adds a new column age to the users table.

How to SELECT data from a table
To select data from a table, you use the SELECT statement. Here’s an example:

sql
Copy code
SELECT * FROM users;
This command retrieves all columns from the users table. To select specific columns:

sql
Copy code
SELECT name, email FROM users;
How to INSERT, UPDATE or DELETE data
INSERT data:

sql
Copy code
INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com');
UPDATE data:

sql
Copy code
UPDATE users SET email = 'new.email@example.com' WHERE name = 'John Doe';
DELETE data:

sql
Copy code
DELETE FROM users WHERE name = 'John Doe';
What are subqueries
Subqueries are SQL queries nested inside another query. They are used to perform operations that depend on the results of another query. For example:

sql
Copy code
SELECT name FROM users WHERE id IN (SELECT user_id FROM orders WHERE order_date = '2024-05-20');
This subquery retrieves the names of users who made orders on '2024-05-20'.

How to use MySQL functions
MySQL functions are built-in functions that perform operations on data. Examples include:

String functions:

sql
Copy code
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;
Numeric functions:

sql
Copy code
SELECT ROUND(price, 2) FROM products;
Date functions:

sql
Copy code
SELECT NOW();
Aggregate functions:

sql
Copy code
SELECT COUNT(*) FROM users;
These functions help in manipulating and retrieving data in a more efficient way.

By understanding and mastering these concepts, you will be well-equipped to work with MySQL and relational databases effectively.
