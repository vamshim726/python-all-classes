

nums=[10,2,6,8,44,5,3,6]

for i in range(1,len(nums)):

    key=nums[i]
    j=i-1

    while(j>=0 and nums[j]>key):
        nums[j+1]=nums[j ]
        j-=1
    nums[j+1]=key
print(nums)
