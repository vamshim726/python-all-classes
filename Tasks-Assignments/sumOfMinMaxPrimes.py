
numbers = input().split()

minPrime=float("inf")
maxPrime=float("-inf")

for num in numbers:
    n = int(num)
    for i in range(2,(n//2)+1):
        if n%i==0:
            break
    else:
        if n < minPrime:
            minPrime=n
        if n > maxPrime:
            maxPrime =n 
if minPrime == float("inf"):
    print("No prime numbers found")
else:
    print("Sum of max and min prime: ", (maxPrime+minPrime))