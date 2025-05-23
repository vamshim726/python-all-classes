n = int(input())

scores=[int(i) for i in input().split() ]

max, secondMax= float('-inf'),float('-inf')




for i in scores:
    if i > max:
        secondMax=max
        max=i
    elif i>secondMax and i !=max:
        secondMax=i

print(secondMax)