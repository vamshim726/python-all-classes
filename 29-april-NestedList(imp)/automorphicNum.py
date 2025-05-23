
# n = input()
# num=int(n)

for i in range(1,1001):
    lenofnum= len(str(i))
    if (i*i)%(10**lenofnum) == i:
        print(i)
    
