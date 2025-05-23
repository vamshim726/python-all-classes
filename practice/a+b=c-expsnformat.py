

# abhithaninu






















num="181"
sum=0

for i in range(len(num)):
    if i<len(num)-1:
        print(num[i],end="+")
    else:
        print(num[i],end="=")
    sum+=int(num[i])
print(sum)