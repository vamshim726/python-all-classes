
str1=input()
vowels="aeiouAEIOU"

vc=0
cc=0

for i in str1:
    if i in vowels:
        vc+=1
    else:
        cc+=1


if cc>vc:
    print("cons are more")

else:
    print("vows more")