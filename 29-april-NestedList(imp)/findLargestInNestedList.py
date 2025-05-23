
n= int(input("Enter a sublist size:")) 
sublist=[]
maxlist=[]

for i in range(n):

    sub=[]
    maxnum=float('-inf')
    while True:
        ele = input()
        if ele=="":
            break
        
        if int(ele)>maxnum:
            maxnum=int(ele)
        sub.append(int(ele))
    maxlist.append(maxnum)
    sublist.append(sub)


print(f"All sublist elements: {sublist}")
print(f"All amx elements in each sublist {maxlist}")