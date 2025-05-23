
n = int(input("enter sublist size : "))

totallist=[]
maxMinList=[]

for i in range(n):

    sublist=[]

    while True:
        ele = input()
        if ele=="":
            break
        sublist.append(int(ele))

    totallist.append(sublist)
    if i%n==0:
        maxMinList.append(min(sublist))
    else:
        maxMinList.append(max(sublist))
print(maxMinList)