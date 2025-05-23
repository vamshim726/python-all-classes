# str1= input().split()
# str2=" ".join(str1[::-1])
# print(str2)






#no methods approach

str1=input() #this is python
 
res=""
for i in range(len(str1)-1,-1,-1):
    if str1[i]==" ":
        print(f"{res} ",end="")
        res=""
    else:
        res=str1[i]+res 
    

print(res)


