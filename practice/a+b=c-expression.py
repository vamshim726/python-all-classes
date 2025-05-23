num = input()
add=0
for i in range(len(num)):
    if i< len(num)-1:
        print(num[i],end="+")
    else:
        print(num[i],end="=")
print(add)