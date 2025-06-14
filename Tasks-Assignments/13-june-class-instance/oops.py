'''
 
Practice Program on OOP'S

Q1. Define a class Employee with the following requirements:
	•	It should have instance variables: name, id, and salary.
	•	Create a method set_details(self, name, emp_id, salary) to assign values to instance variables.
	•	Create a method display_details(self) to print all employee details.

✨ Task: Create 3 employee objects and set/display their details.


Q2. Add the following to your Employee class:
	•	Add a method apply_bonus(self, percentage) which increases the salary by the given bonus percentage.

✨ Task: Apply a 10% bonus to all employees and display updated salary.

'''


class Employee:
    def __init__(self):
        self.name = ""
        self.emp_id = 0
        self.salary = 0.0

    def set_details(self, name, emp_id, salary):
        self.name=name
        self.emp_id =emp_id
        self.salary=salary
    
    def display_details(self):
        print(f"Name: {self.name}, Id: {self.emp_id }, Salary: {self.salary}")


emp1=Employee()
emp2=Employee()
emp3=Employee()


emp1.set_details("jhon",202,45000)
emp1.display_details()

emp2.set_details("alice",203,5000)
emp2.display_details()

emp3.set_details("bob",204,65000)
emp3.display_details()




def apply_bonus(self, percentage):
    self.salary+= percentage* self.salary /100

Employee.apply_bonus=apply_bonus

emp1.apply_bonus(10)
emp2.apply_bonus(10)
emp3.apply_bonus(10)


print("\n🔹 Updated Salaries After Bonus:\n")

emp1.display_details()
emp2.display_details()
emp3.display_details()
