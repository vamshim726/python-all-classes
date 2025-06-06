

nums=[10,20,30,40,60,70,80]
ele=50
indx=4

nums.append(0)

for i in range(len(nums)-1,indx,-1):
    nums[i]=nums[i-1]

nums[indx]=ele

print(nums)


#approach 2
nums2=[10,20,30,40,60,70,80]

nums2=nums2[:indx]+[ele]+nums2[indx:]
print(nums2)


# approach3
nums4=[10,20,30,40,60,70,80]

newNums=[]
for i in range(len(nums4)):
    if i ==indx:
        newNums.append(ele)
    newNums.append(nums4[i])

print(newNums)
