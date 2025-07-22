'''
Practice Program

Problem Statement:
You are building an employee management system where:
* Person is the base class that stores basic info like name and age.
* Employee inherits from Person and stores additional info like employee ID and salary.
* Manager inherits from Employee and stores manager-specific info like team size.

1) Create a base class Person with:
  Attributes: name, age
  Method: display_person_info()

2) Create a subclass Employee (inherits from Person) with:
  Attributes: employee_id, salary
  Method: display_employee_info() that uses super() to call     base class method

3) Create a subclass Manager (inherits from Employee) with:
  Attribute: team_size
  Method: display_manager_info() that calls     display_employee_info() using super()


'''



class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):

    def __init__(self,name, age,employee_id,salary):
        super().__init__(name,age) 
        self.employee_id=employee_id
        self.salary=salary

    def display_employee_info(self):
        super().display_person_info()
        print(f"Id {self.employee_id}, Salary: {self.salary}")
class Manager(Employee):

    def __init__(self,name, age,employee_id,salary,team_size):
        super().__init__(name, age,employee_id,salary)
        self.team_size=team_size

    def display_manager_info(self):
        super().display_employee_info()
        print(f"Team size {self.team_size}")
     

e1=Employee("ram",20,545,10000)
e1.display_employee_info()
 

m1=Manager("raj",33,533,20000,9)
m1.display_manager_info()