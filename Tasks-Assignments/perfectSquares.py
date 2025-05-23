#print perfect square

nums=[int(i) for i in input().split()]

for num in nums:
    j = 1
    while j * j <= num:
        if j * j == num:
            print(num, end=" ")
            break
        j += 1