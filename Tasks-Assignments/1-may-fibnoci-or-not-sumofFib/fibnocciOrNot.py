
'''
WAP to check whether a number is fibonacci number or not 

input: Enter a number: 8
output: It is a Fibonacci number

input: Enter a number: 10
output: No it is not a Fib number


'''
num = int(input("Enter a number :"))

a,b=0,1
isFibonocci=False

while a<=num :
    if num == a:
        isFibonocci=True
        break
    a,b=b,a+b

 
print("It is a Fibonacci number" if isFibonocci else "No it is not a Fibonacci number")


