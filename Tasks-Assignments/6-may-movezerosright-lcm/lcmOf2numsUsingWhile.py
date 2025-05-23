'''
2) Program to print LCM of given numbers using while loop

input: 2 8 4
output: LCM : 8

'''


nums=[int(i) for i in input().split()]

num1=nums[:1]


def findLcm(num1,num2):
    max1 = num1 if num1>num2 else num2
    while True:
        if max1%num1 == 0 and max1%num2==0:
            return max1
        max1+=1

res=nums[0]


#using while
i = 1
while i < len(nums):
    res = findLcm(res, nums[i])
    i += 1

print("LCM :", res)













#using for

# for i in nums[1:]:
#     res=findLcm(res,i)
#     print(res)

# print("LCM : ",res)
    






 