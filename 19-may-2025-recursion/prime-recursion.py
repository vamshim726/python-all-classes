

#check num is prime or not using recursion

def prime(num,div=2):
    if div==num//2:
        return True
    if num%div==0:
        return False
    return prime(num,div+1)
 
num=int(input())
print(prime(num))