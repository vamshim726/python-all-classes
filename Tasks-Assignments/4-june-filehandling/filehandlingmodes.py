

studentSize=int(input("Enter number of students: "))

studentData=[]
for i in range(studentSize):
    data=input(f"Enter student Data {i+1}: ")
    studentData.append(data)

with open("studentData.txt","w") as file:
    for data in studentData:
        file.write(data+"\n")

 
def findName(name):
    file=open("studentData.txt","r")
    content=file.readlines()

    name_lower = name.lower()
    for i,line in enumerate(content,start=1):
        if name_lower in line.lower():
            print(f"{name} Found at Line {i}")
            break
    
    else:
        print("No data Found")

name=input("Enter student name to Find: ")
findName(name)
