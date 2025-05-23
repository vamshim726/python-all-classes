

# print perfect square in lists

nums = [int(i) for i in input().split()]   #10 16 18 25

for num in nums:
    if num**0.5==int(num**0.5):
        print(num,end=" ")