# sqlalchemy-challenge
SQLAlchemy Homework - Surfs Up!
![image of HW](https://github.com/BPayne-216/sqlalchemy-challenge/blob/master/EmployeeSQL/logo.png)

This project utilizes SQL (PostgreSQL) to review an employee database of a corporation in the 1980s - 1990s.

The motivation of this project allows database analysts to quickly retrieve information for a large corporation.  Much of this information are details regarding their employees.  However, this information can be used by management for multiple purpose: budgeting, forecasting, incentives, reviews, and other query-related activity.

Build status: The first part of the project utilized creating an ERD structure.  Using PostgresSQL, tables were built based on the ERD structure.  The tables were populated with 6 different csv files based on similar employee and corporate tables.  8 different queries were made in PostgreSQL that Grouped and Joined the tables.  Next, for the bonus, SQLalchemy was used to bring the data back from PostgreSQL to python and pandas tables.  Pandas tables were made to create two charts, which are in a jupyter notebook.

Technology/Framework (In order): Quickdatabaseddiagrams.com.  
Export both png and SQL structure to create tables.  
Excel csv files were used to populate the tables and then make queries in PostgreSQL.
Python and SQLalchemy used to access the PostgreSQL table information.
Resulting tables and graphs were put into a jupyter notebook.  Matplotlib was used to create graphs.

Features/Files:
(6) csv files used to populate PostgreSQL tables.
QuickDBD.png: ERD schema.
QuickDBD.sql: this is the sql file used to create the SQL tables with appropriate primary and foreign key structure.
QueryResults.sql: this file has the query code and output for the (8) requested employee queries.
hwbonus.ipynb: this jupyter notebook file has the SQLalchemy structure to bring in the SQL tables into pandas.  It also included the dataframes merged to create the charts.
2 final .png files were output as separate files from the Bonus section.
