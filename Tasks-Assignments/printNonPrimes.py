number= input("Enter a number : ")
nonPrimesFound=False

for digit in number:
    num=int(digit)
    for i in range(2,(num//2)+1):
        if num%i==0:
            if nonPrimesFound==False:
                print(f"Non Primes are : {num}",end=" ")
                nonPrimesFound=True
                break
            else:
                print(num,end=" ")
                break
if nonPrimesFound==False:
    print("There are no non Primes")






