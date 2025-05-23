
words= input()

res=""
for i in range(len(words)-1,-1,-1):
    if words[i]==" ":
        print(f"{res}",end=" ")
        res=""
    else:
        res=words[i]+res
print(res)