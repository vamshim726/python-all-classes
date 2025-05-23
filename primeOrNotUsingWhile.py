#  Write a program to check whether a number is prime or not by using a while loop.

# input: Enter a number: 10
# Output: 10 is not a prime number.

# input: Enter a number: 23
# Output: 23 is a prime number.



num = int(input("Enter a Number :"))
 
if num <= 1:
    print(f"{num} is not a prime number")

else:
    i=2
    while i <= (num//2) :
        if num%i==0:
            print(f"{num} is not a prime number" )
            break 
        i+=1
    else:
        print(f"{num} is a prime number")


