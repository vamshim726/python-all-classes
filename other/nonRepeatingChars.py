

# str1="google"

# checked=[]
# counter=[]

# for ch in str1:
#     if ch not in checked:
#         count=0
#         for j in str1:
#             if ch ==j:
#                 count+=1
#         checked.append(ch)
#         counter.append(count)

# print(counter)
# print(checked)

# for i in len(checked):





# for ch in checked:

str1="google"
 
for x in str1:
    count=0
    for y in str1:
        if x==y:
            count+=1
    if count==1:
        print(x)
