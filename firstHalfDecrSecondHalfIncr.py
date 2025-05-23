
nums=[int(i) for i in input().split()]

mid=len(nums)//2
nums.sort()
firstHalf=nums[:mid][::-1]
secondHalf= nums[mid:]

for i in secondHalf:
    firstHalf.append(i)

print(* firstHalf)
