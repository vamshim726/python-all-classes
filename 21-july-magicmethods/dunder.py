

'''
Magic Methods
In Python, there are different magic methods available to perform overloading operations.
The below table shows the magic methods names to overload the mathematical operator, assignment operator, and relational operators in Python.
'''
class Student:
    def __init__(self, name, study_class,subjects,marks):
        self.name=name
        self.study_class=study_class
        self.subjects=subjects
        self.marks=marks

        print(self.name, 'Student object created')
    
    def __add__(self,other_student):
        return self.marks+other_student.marks
    

    def __sub__(self,other_student):
        return self.marks-other_student.marks

    def __str__(self):
        
        return str((self.name,self.study_class,self.subjects,self.marks))
    

    def __len__(self):
        print('subject length is')
        return len(self.subjects)

s1=Student('Alice',9,['M','Phy','Bio','Soc'],85)
s2=Student('Bob',9,['M','Phy','Bio','Soc'],80)

print(s1+s2)
print(s1-s2)
print(s1)
print(len(s1))