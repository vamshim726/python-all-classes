

# str1="this is py"


# revStr=""
# for i in range(len(str1)-1,-1,-1):
#     if str1[i] ==" ":
#         print(f"{revStr} ",end="")
#         revStr=""
#     else:
#         revStr=str1[i]+revStr
# print(revStr)












str1="this is python"

rev=""

for i in str1[::-1]:
    if i==" ":
        print(rev,end=" ")
        rev=""
    else:
        rev=i+rev
print(rev)








