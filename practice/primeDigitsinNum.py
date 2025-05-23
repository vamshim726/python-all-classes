

num = input() #533
nonp=""

for i in num:
    n=int(i)
    for j in range(2,(n//2)+1):
        if n%j==0:
            nonp+= str(n)+" "
            break
if nonp=="":
    print("no non primes")
else:
    print(nonp)