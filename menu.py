import sqlite3
import hrsys
import employee

while True:
    print("\n Menu:")
    print("**********")
    print(" 1. Create table Employee")
    print(" 2. Insert single record into Employee")
    print(" 3. Bulk insert records into Employee")
    print(" 4. Display all employees from Employee")
    print(" 5. Search an employee")
    print(" 6. Update a single record")
    print(" 7. Delete a single record")
    print(" 8. Bulk delete")
    print(" 9. Delete a table")
    print(" 10. Statistic")
    print(" 11. Exit\n")

    __choose_menu = int(input("Enter your choice: "))
    db_ops = hrsys.DBOperations()
    if __choose_menu == 1:
        db_ops.create_table()
    elif __choose_menu == 2:
        db_ops.insert_data()
    elif __choose_menu == 3:
        db_ops.bulk_insert()
    elif __choose_menu == 4:
        db_ops.select_all()
    elif __choose_menu == 5:
        db_ops.search_data()
    elif __choose_menu == 6:
        db_ops.update_data()
    elif __choose_menu == 7:
        db_ops.delete_data()
    elif __choose_menu == 8:
        db_ops.bulk_delete()
    elif __choose_menu == 9:
        db_ops.delete_table()
    elif __choose_menu == 10:
        db_ops.statistic_data()
    elif __choose_menu == 11:
        exit(0)
    else:
        print("Invalid Choice")