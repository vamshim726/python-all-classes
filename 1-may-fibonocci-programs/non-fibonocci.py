
#print n non fibonocci number

n =int(input())

a,b=0,1

nonfib=0

while nonfib!=n:

    for i in range(a+1,b):
        if nonfib==n:
            break
        print(i)
        nonfib+=1
    a,b=b,a+b