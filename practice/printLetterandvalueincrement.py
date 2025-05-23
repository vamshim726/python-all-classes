str1=input()
cnt=1
for i in str1: 
    if i>='A' and i<='Z' or i>='a' and i<='z':
        print(f"{i}{cnt}",end="")
        cnt+=1