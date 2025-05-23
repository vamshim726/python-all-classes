

numbers = input().split()

minPrime=float('inf')

for num in numbers:
    n= int(num)
    if n > 1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            if n < minPrime:
                minPrime=n 
if minPrime == float('inf'):
    print("There are no Prime Numbers")
else:
    print("Minimum Prime: ",minPrime)