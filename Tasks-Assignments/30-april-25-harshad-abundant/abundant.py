# https://takeuforward.org/data-structure/check-if-the-number-is-an-abundant-number-or-not/

num = int(input())

sum=0

for i in range(1,(num//2)+1):
    if num%i==0:
        sum+=i
print("Abundant NUmber" if sum>num else "Not Abandant Number")

