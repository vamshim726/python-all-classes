str1="hi all! how are you?"

cnt=1
for i in range(len(str1)):
    if str1[i]>="a" and str1[i]<="z" or str1[i]>="A" and str1[i]<="Z":
        print(f"{str1[i]}{cnt}",end="")
        cnt+=1