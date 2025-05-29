

str1="abcdxZyz"

res=""
for i in str1:
    if ord(i)==ord("z"):
        res+=chr(ord("a"))
    elif ord(i)==ord("Z"):
        res+=chr(ord("A"))
    else:
        res+=chr(ord(i)+1)

    
print(res)

