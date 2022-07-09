
class Employee:
    def __init__(self):
        self.employeeID = 0
        self.title = ''
        self.forename = ''
        self.surname = ''
        self.email = ''
        self.salary = 0.0

    def set_employee_id(self, employeeID):
        self.employeeID = employeeID

    def set_employee_title(self, title):
        self.title = title

    def set_forename(self, forename):
        self.forename = forename

    def set_surname(self, surname):
        self.surname = surname

    def set_email(self, email):
        self.email = email

    def set_salary(self, salary):
        self.salary = salary

    def get_employee_id(self):
        return self.employeeID

    def get_employee_title(self):
        return self.title

    def get_forename(self):
        return self.forename

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email

    def get_salary(self):
        return self.salary

    def __str__(self):
        return str(
            self.employeeID) + "\n" + self.title + "\n" + self.forename + "\n" + self.surname + "\n" + self.email + "\n" + str(
            self.salary)