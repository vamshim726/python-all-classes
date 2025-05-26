
num=int(input())
if num>1:
    for i in range(2,(num//2)+1):
        if num %i==0:
            print("not prim")
            break
    else :
        print("prim")

else:
    print("enter valid")