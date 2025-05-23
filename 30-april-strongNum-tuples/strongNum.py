# http://takeuforward.org/data-structure/check-if-a-number-is-a-strong-number-or-not/

# nums = input()

# res=0

# for num in nums:
#     prod =1
#     for i in range(1,int(num)+1):
#         prod*=i
#     res+=prod

# print("strong num" if int(nums)==res else "not strong num")



# appraoch 2


nums = int(input())
temp=nums
res=0

while nums > 0:
    digit = nums % 10
    prod=1
    for i in range (1,digit+1):
        prod*=i
    res+=prod
    nums//=10

if res==temp:
    print("strong number")
else:
    print("not strong number")
    
