import employee
import sqlite3
import re

class DBOperations:

    # These fields are used for sqlite queries
    sql_create_table_firsttime = """CREATE TABLE IF NOT EXISTS Employee(
    employeeID INTEGER NOT NULL PRIMARY KEY,
    title TEXT,
    forename TEXT,
    surname TEXT,
    email VARCHAR,
    salary REAL
    )"""
    sql_create_table = """CREATE TABLE Employee(
    employeeID INTEGER NOT NULL PRIMARY KEY,
    title TEXT,
    forename TEXT,
    surname TEXT,
    email VARCHAR,
    salary REAL
    )"""
    sql_insert = "INSERT INTO Employee VALUES (:employeeID,:title,:forename,:surname,:email,:salary) "
    sql_select_all = "SELECT * FROM Employee"
    sql_search = "SELECT * FROM Employee WHERE employeeID =:employeeID"
    sql_update_id = "UPDATE Employee SET 'employeeID'=:newID WHERE employeeID=:oldID"
    sql_update_title = "UPDATE Employee SET 'title'=:title WHERE employeeID=:employeeID"
    sql_update_forename = "UPDATE Employee SET 'forename'=:forename WHERE employeeID=:employeeID"
    sql_update_surname = "UPDATE Employee SET 'surname'=:surname WHERE employeeID=:employeeID"
    sql_update_email = "UPDATE Employee SET 'email'=:email WHERE employeeID=:employeeID"
    sql_update_salary = "UPDATE Employee SET 'salary'=:salary WHERE employeeID=:employeeID"
    sql_delete_data = "DELETE From Employee WHERE employeeID =:employeeID"
    sql_drop_table = "DROP TABLE Employee"
    sql_sort_all_asc = "SELECT * FROM Employee ORDER BY salary ASC"
    sql_sort_all_desc = "SELECT * FROM Employee ORDER BY salary DESC"
    sql_average_salary = "SELECT AVG(salary) FROM Employee"
    sql_max_salary = "SELECT * FROM Employee WHERE salary= (SELECT MAX(salary) FROM Employee)"
    sql_min_salary = "SELECT * FROM Employee WHERE salary= (SELECT MIN(salary) FROM Employee)"
    sql_sum_salary = "SELECT SUM(salary) FROM Employee"

    # initialize the database
    def __init__(self):
        try:
            self.conn = sqlite3.connect("DBName.db")
            self.cur = self.conn.cursor()
            self.cur.execute(self.sql_create_table_firsttime)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # get_connection is used to make connection with the database.
    def get_connection(self):
        self.conn = sqlite3.connect("DBName.db")
        self.cur = self.conn.cursor()

    # create_table is used to create the table
    def create_table(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_create_table)
            self.conn.commit()
            print("Table created successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # insert_data function is used to insert a single record.
    def insert_data(self):
        try:
            self.get_connection()

            emp = employee.Employee()

            emp.set_employee_id(int(input("Enter Employee ID: ")))
            emp.set_employee_title(input("Enter Employee title: "))
            emp.set_forename(input("Enter Employee forename: "))
            emp.set_surname(input("Enter Employee surname: "))
            emp.set_email(input("Enter Employee email: "))   
            emp.set_salary(float(input("Enter Employee salary: ")))

            self.cur.execute(self.sql_insert,
                             {'employeeID': emp.get_employee_id(), 'title': emp.get_employee_title(),
                              'forename': emp.get_forename(), 'surname': emp.get_surname(),
                              'email': emp.get_email(), 'salary': emp.get_salary()})

            self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # bulk_insert function is used to insert multiple records.
    # This function allow users to continuously input value of each record by "," and use "enter" to enter next record
    # The number of records is defined by user.
    def bulk_insert(self):
        try:
            self.get_connection()

            emp = employee.Employee()
            number=int(input("please enter the number of record you would like to insert: "))
            print("please enter employeeID,title,forename,surname,email,salary and separate them by a comma.Press "
                  "enter to start a new record. Input limit: 3 records")
            print("""e.g.
            001,Miss,forename1,surname1,email1,salary1
            002,Mr,forename2,surname2,email2,salary2
            003,Ms,forename3,surname3,email3,salary3
            """)
            for i in range(number):
                record = input()
                mylist = list(record.split(","))
                emp.set_employee_id(int(mylist[0]))
                emp.set_employee_title(mylist[1])
                emp.set_forename(mylist[2])
                emp.set_surname(mylist[3])
                emp.set_email(mylist[4])
                emp.set_salary(mylist[5])

                self.cur.execute(self.sql_insert,
                                 {'employeeID': emp.get_employee_id(), 'title': emp.get_employee_title(),
                                  'forename': emp.get_forename(), 'surname': emp.get_surname(),
                                  'email': emp.get_email(), 'salary': emp.get_salary()})

                self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # select_all function is used to display all the records from the employee table
    def select_all(self):
        try:
            self.get_connection()
            self.cur.execute(self.sql_select_all)
            results = self.cur.fetchall()
            if len(results) == 0:
                print("no table is found")
            else:
                for record in results:
                    for column in record:
                        print(column,"|",end="")
                    print("\n","-----------------------------------------")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # search_data function is used to search a single record by the employee ID from user input.
    def search_data(self):
        try:
            self.get_connection()
            employeeID = int(input("Enter Employee ID: "))
            self.cur.execute(self.sql_search, {'employeeID': employeeID})
            result = self.cur.fetchone()
            if result is None:
                print("no records found")
            else:
                for index, detail in enumerate(result):
                    if index == 0:
                        print("Employee ID: " + str(detail))
                    elif index == 1:
                        print("Employee Title: " + detail)
                    elif index == 2:
                        print("Employee Name: " + detail)
                    elif index == 3:
                        print("Employee surname: " + detail)
                    elif index == 4:
                        print("Employee email: " + detail)
                    else:
                        print("salary: " + str(detail))

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # update function is used to update the corresponding field by user's choice in single record.
    # user can update the value of the 6 attributes of the Employee table
    def update_data(self):
        try:
            self.get_connection()
            continue_update = True
            while continue_update:

                employeeID = int(input("Enter Employee ID: "))
                self.cur.execute(self.sql_search, {'employeeID': employeeID})
                result = self.cur.fetchone()
                if result is None:
                    print("no records found")
                else:
                    print("1.Update Employee ID")
                    print("2.Update Employee Title")
                    print("3.Update Employee forename")
                    print("4.Update Employee surname")
                    print("5.Update Employee email")
                    print("6.Update salary")
                    option = int(input("Please enter a number:"))
                    if option == 1:
                        new_id = int(input("Please enter new ID: "))
                        self.cur.execute(self.sql_update_id, {'newID': new_id, 'oldID': employeeID})
                        self.conn.commit()
                        print("Update successfully")

                    elif option == 2:
                        new_title = str(input("Please enter new title: "))
                        self.cur.execute(self.sql_update_title, {'title': new_title, 'employeeID': employeeID})
                        self.conn.commit()
                        print("Update successfully")

                    elif option == 3:
                        new_forename = str(input("Please enter new forename: "))
                        self.cur.execute(self.sql_update_forename, {'forename': new_forename, 'employeeID': employeeID})
                        self.conn.commit()
                        print("Update successfully")

                    elif option == 4:
                        new_surname = input("Please enter new surname: ")
                        self.cur.execute(self.sql_update_surname, {'surname': new_surname, 'employeeID': employeeID})
                        self.conn.commit()
                        print("Update successfully")

                    elif option == 5:
                        new_email = input("Please enter new email: ")
                        self.cur.execute(self.sql_update_email, {'email': new_email, 'employeeID': employeeID})
                        self.conn.commit()
                        print("Update successfully")

                    elif option == 6:
                        new_salary = input("Please enter new salary: ")
                        self.cur.execute(self.sql_update_salary, {'salary': new_salary, 'employeeID': employeeID})
                        self.conn.commit()
                        print("Update successfully")

                print("Would you like to continue updating records? ")
                response = int(input("1.Yes 2.No. Enter number: "))
                if response == 1:
                    continue_update = True
                else:
                    continue_update = False

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # delete_function is used to delete a single record from the table.
    # The user will need to input the employee id to delete the corresponding record.
    def delete_data(self):
        try:
            self.get_connection()
            employeeID = int(input("Enter Employee ID: "))
            self.cur.execute(self.sql_search, {'employeeID': employeeID})
            result = self.cur.fetchone()
            if result is None:
                print("no records found")
            else:
                self.cur.execute(self.sql_delete_data, {'employeeID': employeeID})
                # result = self.cur.fetchone()
                self.conn.commit()
                print("Delete is completed.")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    def bulk_delete(self):
        try:
            self.get_connection()
            print("please enter employeeID and separate them by a comma.")
            print("""e.g.
                        001,002,003
                                """)
            record = input("please enter:")
            mylist = list(record.split(","))
            for id in mylist:
                employeeID = int(id)
                self.cur.execute(self.sql_search, {'employeeID': employeeID})
                result = self.cur.fetchone()
                if result is None:
                    print(str(employeeID) + " is not found")
                else:
                    self.cur.execute(self.sql_delete_data, {'employeeID': employeeID})
                    self.conn.commit()
            print("Delete is completed.")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # delete table function is used to delete the entire table and its data.
    # Table will need to be recreated after this operation.
    def delete_table(self):
        try:
            self.get_connection()
            confirmation = int(input("Would you like to delete the table:\n 1.Yes,delete the table and all the data. "
                                     "2.No, keep the table.\n "))
            if confirmation == 1:
                self.cur.execute(self.sql_drop_table)
                self.conn.commit()
                print("The table is deleted.")

            if confirmation == 2:
                print("Thank you. The table is remain")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()

    # statistic function is used to carry out calculation with the data in employee table.
    def statistic_data(self):
        try:
            self.get_connection()
            continue_update = True
            while continue_update:
                print("1.Sort the table by salary Descend ")
                print("2.Sort the table by salary Ascend")
                print("3.Average salary of all employees")
                print("4.Sum salaries of all employees")
                print("5.Maximum salary among employees")
                print("6.Minimum salary among employees")

                option = int(input("Please enter a number: "))
                if option == 1:
                    self.cur.execute(self.sql_sort_all_desc)
                    results = self.cur.fetchall()
                    for i in results:
                        print(i)

                elif option == 2:
                    self.cur.execute(self.sql_sort_all_asc)
                    results = self.cur.fetchall()
                    for i in results:
                        print(i)
                elif option == 3:
                    self.cur.execute(self.sql_average_salary)
                    result = self.cur.fetchone()[0]
                    print("The average salary of an employee is {}".format(result))
                elif option == 4:
                    self.cur.execute(self.sql_sum_salary)
                    result = self.cur.fetchone()[0]
                    print("The total salary of all employees is {}".format(result))
                elif option == 5:
                    self.cur.execute(self.sql_max_salary)
                    result = self.cur.fetchone()
                    print("ID:{}\ntitle:{}\nforename:{}\nsurname:{}\nemail:{}\nsalary:{}".format(result[0], result[1],
                                                                                                 result[2], result[3],
                                                                                                 result[4], result[5]))
                elif option == 6:
                    self.cur.execute(self.sql_min_salary)
                    result = self.cur.fetchone()
                    print("ID:{}\ntitle:{}\nforename:{}\nsurname:{}\nemail:{}\nsalary:{}".format(result[0], result[1],
                                                                                                 result[2], result[3],
                                                                                                 result[4], result[5]))
                print("Would you like to continue statistics? ")
                response = int(input("1.Yes 2.No. Enter number: "))
                if response == 1:
                    continue_update = True
                else:
                    continue_update = False

        except Exception as e:
            print(e)
        finally:
            self.conn.close()