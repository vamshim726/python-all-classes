num = input()

sum=0
for i in num:
    prod = 1
    for j in range(1,int(i)+1):
        prod=prod*j
    sum=sum+prod

if num==str(sum):
    print("strong")
else:
    print("not strong")