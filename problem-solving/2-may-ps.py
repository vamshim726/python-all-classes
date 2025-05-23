# #1st

# # list to map 

# s3 = ["name", "pin", "fees"]
# s4 = ["python", 101, 2500]

# d1 = {}
# for i in range(len(s3)):
#     d1[s3[i]] = s4[i]
# print("d1: ",d1)

# #  or using zip method

# d2=dict(zip(s3,s4))
# print("d2: ",d2)


# #2nd
# #insert length of string in same position
# s1=["python","java","developer"]
  
# for i in range(len(s1)):
#     s1[i]= len(s1[i])

# print(s1)


# #3rd
# #print with quotes ''
# s="'pythondeveloper'"
# print(s)


 
#4th
#swap last with first

s5=[10,20,30,40,50,60,70,80]

s=0
e=len(s5)-1

while s<e:
    print(s5[s])
    s5[s],s5[e]= s5[e],s5[s]
    s+=1
    e-=1
print(s5)
 

#  5th 
# palindrome or not


num=125

temp=num
rev=0

while num !=0:
    ld=num%10
    rev=rev*10+ld
    num//=10

print("palindrome" if rev==temp else "not palindrome")


#6 user define function
def lengthOfList(lst):
    count=0
    for i in lst:
        count+=1
    return count

print(lengthOfList([1,2,3,4,5]))



#7 username or email any 1, password is must 
username="vamshi"
email="vamshi@gmail.com"
password="12345"

user1=input()
e1=input()
pass1=input()

if user1 == username or email==e1 and password==pass1:
    print("login success")
else:
    print("login failed")








 




 