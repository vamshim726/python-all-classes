'''
WAP to print sum of fib numbers in the given numbers
'''

nums = [int(i) for i in input().split()]
 
sumOfFib=0
for num in nums:
    a,b=0,1
    isFib = False

    while a<=num:
        if a==num:
            isFib=True
            break
        a,b=b,a+b

    if isFib:
        sumOfFib+=num

print(sumOfFib)