# sqlalchemy-challenge
SQLAlchemy Homework - Surfs Up!
![image of HW](https://github.com/BPayne-216/sqlalchemy-challenge/blob/master/Images/surfs-up.png)

This project utilizes SQL (PostgreSQL) to review an employee database of a corporation in the 1980s - 1990s.

The motivation of this project is to utilize database tables from SQLite format and in Python to analyze temperature and Weather Stations.  Queries were made to review smaller samples of the database tables and build smaller time series graphs. 

Build status: The first part saved the sqlite files and using SQLalchemy creating.  SqlAlchemy was used to bring and query the database within the python application.  Many of the queries were transferred to pandas dataframes.  Matplotlib was also used to create graphs.

Technology/Framework (In order):  
Python, Pandas, Matplotlib.
Flask was used within Python to use the database queries and create APIs Routes.

Features/Files:
climate_starter.ipynb contains Step 1 and Step 2 of the Climate and Station analysis.
Precipitation_Analysis_png and Station_Histogram.png are files that have the output for steps 1 and 2.
QuickDBD.sql: this is the sql file used to create the SQL tables with appropriate primary and foreign key structure.
app.py is the python file that contains the Flask code that accesses the hawaii.sqlite tables, used to create Routes for the Climate App.  This file contains JSON (jsonify) and ORM processes.
