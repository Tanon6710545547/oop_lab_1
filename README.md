# OOP Programming Laboratory 2

## Overview
This lab focuses on converting procedural code from **Commit 2** into an **object-oriented design** by using Python classes.

You are required to implement two main classes: **DataLoader** and **Table**, following the design shown in class and the example below.

---

## Project Structure
```
oop_lab_2/
│── README.md
│── Cities.csv
│── data_processing.py
```

---

## Design Overview

### Class: `DataLoader`
**Purpose:**  
Handles loading CSV data files.

**Attributes:**
- `base_path`: the base directory where data files are stored.

**Methods:**
- `__init__(base_path=None)`  
  Initialize the DataLoader with a base path for data files.
- `load_csv(filename)`  
  Load a CSV file and return its contents as a list of dictionaries.

---

### Class: `Table`
**Purpose:**  
Represents tabular data and provides filtering and aggregation functionalities.

**Attributes:**
- `name`: the table name.  
- `dict_list`: list of dictionaries containing data rows.

**Methods:**
- `filter(condition_func)`  
  Returns a new `Table` object containing only rows that satisfy the given condition.
- `aggregate(agg_func, column_name)`  
  Applies an aggregate function to a specific column (e.g., average, max, count).

---

## How to Test and Run
1. Place `Cities.csv` in the same folder as `data_processing.py`.
2. Run the following command:
   ```
   python data_processing.py
   ```
3. The output should display:
   - The average temperature of all cities.
   - A list of all cities in Germany.
   - All cities in Spain with temperature above 12°C.
   - The number of unique countries.
   - The average temperature of all cities in Germany.
   - The max temperature of all cities in Italy.

---

## Example Output
```
9.497840375586858

All the cities in Germany:
['Augsburg', 'Germany']
['Berlin', 'Germany']
...

The number of unique countries is:
37

The average temperature of all the cities in Germany:
7.869285714285714

The max temperature of all the cities in Italy:
17.9
```
