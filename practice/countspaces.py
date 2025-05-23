str1="aaaaa bbbbb "
vc,cc,sc=0,0,0
vowels="aeiouAEIOU"

for i in range(len(str1)):
    if str1[i]==" ":
        sc+=1
    elif str1[i] in vowels:
        vc+=1
    else:
        cc+=1

print(vc,cc,sc)