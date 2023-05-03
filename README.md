# HR System
This repository contains a simple HR system implemented in Python, using SQLite as the database to manage employee records. The system allows users to perform various operations, such as adding, updating, searching, and deleting employee data, as well as generating basic statistics.

## Structure
The project is organized into the following files:

1. `menu.py`: Contains the main menu interface for the user to interact with the HR system.
2. `hrsys.py`: Contains the core functionality of the HR system, including functions for database operations and employee management.
3. `employee.py`: Contains the Employee class, representing an employee object with its attributes and methods.

## Requirements
Python 3.x

## Usage
To run the HR system, execute the following command:

```
python menu.py
```

The system will present a menu with various options for managing employee records:

1. Create table
2. Insert data
3. Bulk insert
4. Select all
5. Search data
6. Update data
7. Delete data
8. Bulk delete
9. Delete table
10. Statistic data
11. Exit

Choose an option by entering the corresponding number and follow the prompts to perform the desired operation.

## Notes
* The system uses SQLite as the database engine. It will create a database file named DBName.db in the same directory as the application.
* When running the system for the first time, choose option 1 to create the employee table before performing any other operations.
* The employee email must be valid according to the provided regex pattern. If the email is not valid, the system will prompt the user to enter a valid email.
* Bulk insert and bulk delete options allow users to enter multiple records separated by commas.
* The statistic data option provides several calculations on employee salary data, such as sorting, average, sum, maximum, and minimum.
