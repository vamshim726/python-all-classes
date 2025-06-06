nums=[5,3,1,4,2]

for i in range(1,len(nums)):
    j=i-1
    key=nums[i]

    while j>=0 and key < nums[j]:
        nums[j+1]= nums[j]
        j-=1
    nums[j+1]=key

print(nums)
