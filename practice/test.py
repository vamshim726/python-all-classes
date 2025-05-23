
str1="this is py" # py is this
res=""

for i in range(len(str1)-1,-1,-1):
    if str1[i] ==" ":
        print(res,end=" ")
        res=""
    else:
        res=str1[i]+res
print(res)