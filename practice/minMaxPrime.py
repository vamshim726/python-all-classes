

nums= [int(i) for i in input().split()]
maxPrime=float('-inf')
minPrime=float('inf')

for i in nums:
    num=int(i)
    for j in range(2,(num//2)+1):
        if num%j==0:
            break
    else:
        if num>maxPrime:
            maxPrime=num
        
        if num<minPrime:
            minPrime=num

print(maxPrime+minPrime)