str1=input()
num=''
for i in str1:
    if i.isdigit():
        num+=i 
    elif i.isalpha():
        if num:
            print(num,end=" ")
            num=""
if num:
    print(num,end=" ")