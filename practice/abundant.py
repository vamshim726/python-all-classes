

num=int(input())

sum=0
for i in range(1,(num//2)+1):
    if num%i==0:
        sum+=i
print(sum)
if  sum>num:
    print("abundant num")
else:
    print("not abundent")