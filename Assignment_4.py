class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

# data

    def __str__(self):


        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeTable:

    def __init__(self):
        self.employees = []

    def add_employee(self, emp):

        self.employees.append(emp)

    def search_by_age(self, age):

        return [emp for emp in self.employees if emp.age == age]

    def search_by_name(self, name):

        return [emp for emp in self.employees if emp.name == name]



    def search_by_salary(self, operator, salary):

        if operator == ">":
            return [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<":
            return [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">=":
            return [emp for emp in self.employees if emp.salary >= salary]
        elif operator == "<=":

            return [emp for emp in self.employees if emp.salary <= salary]


table = EmployeeTable()
table.add_employee(Employee("161E90", "raman", 41, 56000))
table.add_employee(Employee("161F91", "himadri", 38, 67500))
table.add_employee(Employee("161F99", "jaya", 51, 82100))
table.add_employee(Employee("171E20", "tejas", 30, 55000))
table.add_employee(Employee("171G30", "ajay", 45, 44000))




search_param = input("Enter the search parameter (1. age, 2. name, 3. salary): ")
if search_param == "1":
    age = int(input("Enter the age to search: "))
    results = table.search_by_age(age)
elif search_param == "2":
    name = input("Enter the name to search: ")
    results = table.search_by_name(name)
elif search_param == "3":
    operator = input("Enter the operator (>, <, >=, <=): ")
    salary = int(input("Enter the salary to search: "))
    results = table.search_by_salary(operator, salary)


if len(results) > 0:
    print(f"Search results ({len(results)}):")
    for result in results:
        print(result)
else:
    print("No results found.")
