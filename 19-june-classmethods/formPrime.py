'''Problem: Given a number n, express the number as a sum of 2 prime numbers.

Examples:

Example 1:
Input : N = 74
Output : True . 
Explanation: 74 can be expressed as 71 + 3 and both are prime numbers. 

Example 2:
Input : N = 11
Output : False. 
Explanation: 11 cannot be expressed as sum of two prime numbers.'''


def isPrime(n):
    if n < 2:
        return False

    for i in range(2,(n//2)+1):
        if n%i==0:
            return False    
    return True

def isExpressedSumOf2(n,found):

    for i in range(n-1,-1,-1):
        if isPrime(i) and isPrime(n-i):
            found=True
    
    return found
 

n= int(input())
found=False
print(True if isExpressedSumOf2(n,found) else False)
 