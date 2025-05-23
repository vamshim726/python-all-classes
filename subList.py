n=int(input("enter size of sublist :"))
sublst=[]

for i in range(n):
    sub=[]
    while True:
        ele = input()
        if ele=="":
            break
        sub.append(ele)
    sublst.append(sub)

print(sublst)