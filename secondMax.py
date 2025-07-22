# n = int(input())

scores=[int(i) for i in input().split() ]

max, secondMax= float('-inf'),float('-inf')

for i in scores:
    if i > max:
        secondMax=max
        max=i
    elif i>secondMax and i !=max:
        secondMax=i

print(secondMax)









#
# def findSecondMax(lst):
#     m=float('-inf')
#     sm=float('-inf')
#     for i in lst:
#         if i>m:
#             sm=m
#             m=i
#         elif i>sm and i!=m:
#             sm=i
#
#     return sm
#
# nums= list(map(int,input().split()))  #or nums=[ int(i) for i in input().split()]
#
# print(nums)
# print(findSecondMax([2,3,5,7,8,5,1]))








