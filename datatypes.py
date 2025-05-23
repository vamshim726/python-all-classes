
#int
num = int(input("Enter a number :"))
print("{} {}".format(num, type(num)))

#float
balance = float(input("Enter a value :"))
print("{} {}".format(balance, type(balance)))

#complex
value = complex(input("Enter a value :"))
print("{} {}".format(value, type(value)))
print("Imaginary part: {}".format(value.imag))
print("Real part: {}".format(value.real))

#string
name= input("Enter a String :")
print("{} {} ".format(name, type(name)))

#boolean
status= bool(input("Enter the status :"))
print("{} {}".format(status,type(status)))


#list
l1=  [10,20,"as",2.0]
print("{} {}".format(l1,type(l1)))

#tuple
t1= (10,20,30,40,(5,6),"@")
print("{} {}".format(t1,type(t1)))

#set
s1= {1,3,5,4,"a"}
print("{} {}".format(s1,type(s1)))

#dict
d1= {"a":10,"b":20,"c":30}
print("{} {}".format(d1,type(d1)))


