
n = int(input("Enter list size"))

nums=[]

for i in range(n):
    sublst=[]
    while True:
        ele = input()
        if ele=="":
            break
        sublst.append(int(ele))
    nums.append(sublst)

print(nums)
    