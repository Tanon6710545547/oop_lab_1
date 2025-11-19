# OOP Programming Laboratory 3

## Lab Overview
This lab demonstrates how to build a simple mini-database system using Object-Oriented Programming (OOP). The system loads CSV files, stores data in tables, and supports basic operations such as filtering, aggregation, and joining, similar to how a real database behaves but implemented manually without SQL or external libraries.

## Project Structure
- Cities.csv: city dataset  
- Countries.csv: country dataset  
- main.py: implementation of DataLoader, DB, and Table classes  
- README.md: documentation  

## Class Overview

### DataLoader
Purpose: Loads CSV files into Python.  
Attributes: base_path (directory of data files).  
Methods:  
- __init__(): sets data directory  
- load_csv(): returns list of dictionaries from a CSV file  

### DB
Purpose: Simple in-memory database storing multiple tables.  
Attributes: tables (dictionary).  
Methods:  
- insert(): stores a Table object  
- search(): retrieves a table by name  

### Table
Purpose: Represents tabular data and provides operations.  
Attributes: table_name, table (list of dictionaries).  
Methods:  
- filter(): returns new Table with rows matching a condition  
- aggregate(): applies an aggregate function to a column  
- join(): combines two tables using a shared key  
- __str__(): displays table contents  

## How to Run
1. Ensure Cities.csv and Countries.csv are in the same folder as main.py.  
2. Run with:  
   python main.py  
3. The program will output results from filtering, joining, and aggregating data, confirming that the mini-database functions correctly.
