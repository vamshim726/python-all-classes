
'''
input : abcd acde
o/p: difference 1+1+1=3



in: abcd abc
op: 1


in: dad badly
out: 3


'''

strs=input().split()

strs.sort(reverse=True,key=len)   #important logic remember, desending order
# print(strs)

res=list(zip(*strs))

# print(res)


out=0
for i in res:
    if len(set(i))!=1:
        out+=1
# print(out)
print(len(strs[0])-len(strs[-1]) + out)

 
#shorter code

out2=sum([1 for i in list(zip(*strs)) if  len(set(i))!=1 ])

print(len(strs[0])-len(strs[-1]) +out2)