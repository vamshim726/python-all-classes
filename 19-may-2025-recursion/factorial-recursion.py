
#find factorial of number using recursion

def factorial(num):
    if num==1 or num==0:
        return 1
    return num*factorial(num-1)

num=int(input())
print(factorial(num))