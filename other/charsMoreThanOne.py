

str1="hithisispythonabft"

for x in str1:
    count=0
    for y in str1:
        if x==y:
            count+=1
    if count>1:
        print(x,end=" ")