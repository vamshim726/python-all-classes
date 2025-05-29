
nums=[10,55,2,36,94,7,55]


for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]

print(nums)