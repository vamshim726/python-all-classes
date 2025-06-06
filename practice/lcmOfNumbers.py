


def findLcm(n1,n2):
    maxn= max(n1,n2)

    while True:
        if maxn%n1==0 and maxn%n2==0:
            return maxn
        maxn+=1
 
nums=[5,6,8]

res=nums[0]
 
for i in range(1,len(nums)):
    res=findLcm(res,nums[i])
 
 
print(res)



