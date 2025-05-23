
num= int(input("Enter a number :"))

a,b=0,1
 
 
# while a<=num:
#     print(a,end=" ")
#     a,b=b,a+b 
 
for _ in range(num):  # You can use any large range
    if a > num:
        break
    print(a, end=" ")
    a, b = b, a + b
