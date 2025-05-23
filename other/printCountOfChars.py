

str1="thisispython"

check=""

for x in str1:
    if x not in check:
        count=0
        for y in str1:
            if x==y:
                count+=1
                check+=x
        print(f"{x}={count}",end=" ")

 