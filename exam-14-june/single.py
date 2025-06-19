

nums=[int(i) for i in input().split()]
d1=dict()


for i in  nums:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1

for i in d1:
    if d1[i]==1:
        print(i)
        break







    