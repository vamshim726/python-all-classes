

class Student:
    def details(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    
    def display(self):
        print(f"name:{self.name} , age:{self.age}, city:{self.city}")

    def updateAge(self,newage):
        self.age=newage
    
    def addDetails(self,pincode):
        self.pincode=pincode
s1=Student()
s2=Student()
s1.details("vamshi",22,"hyd")
s2.details("rahu",23,"warangal")


print(s1.name)

print(getattr(s1,"name"))
print(getattr(s1,"city"))


s1.addDetails("50324")
print(s1.__dict__)
print(s2.__dict__)


def addDetailsFormoutside(self,id):
    self.id=id

Student.addDetailsFormoutside=addDetailsFormoutside
s1.addDetailsFormoutside(202)
print(s1.__dict__)
print(s2.__dict__)
print(Student.__dict__)

