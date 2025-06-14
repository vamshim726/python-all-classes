# Problem Statement: Given an array of N integers, the task is to replace each element of the array by its rank in the array.

# Examples:

# Example 1:
# Input: 20 15 26 2 98 6
# Output: 4 3 5 1 6 2
# Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…

# Example 2:
# Input: 1 5 8 15 8 25 9
# Output: 1 2 3 5 3 6 4
# Explanation: When sorted,the array is 1,5,8,8,9,15,25. So the rank of 1 is 1,rank of 5 is 2,rank of 8 is 3 and so…


# approach 1

nums=list(map(int,input().split()))
temp=nums.copy()
nums.sort()
nums=list(set(nums))
# print(nums)
d1=dict()

for i in range(len(nums)):
    d1[i+1]=nums[i]

# print(d1)

for i in temp:
    for key,val in d1.items():
        if i==val:
            print(key, end=" ")

# approach 2



# nums=[int(i) for i in input().split()]

# new_nums=set(nums)
# nums_sorted= sorted(new_nums)
 

# for i in nums:
#     for ind in range(len(nums_sorted)):
#         if i==nums_sorted[ind]:
#             print(ind+1, end=" ")
#             break