num= input("enter a num")#32457

maxEven=float('-inf')
for i in num:
    if int(i)%2==0 and int(i) > maxEven:
        maxEven =int(i)
print(maxEven)