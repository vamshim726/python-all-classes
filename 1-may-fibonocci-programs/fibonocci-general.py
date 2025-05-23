
#print n fibonocci numbers


num = int(input())

a,b=0,1

i=1
while i<=num:
    print(a,end=" ")
    a,b  = b,a+b
    i+=1
    #c=a+b
    #a=b
    #b=c


# good variable names fib program from youtube


# n = int(input())

# n1=0
# n2=1
# count=2

# if n<0:
#     print("enter postive value")
# elif n==1:
#     print(n1)
# else:
#     print(n1)
#     print(n2)

#     while count<n:
#         print(n1+n2)
#         n1,n2=n2,n1+n2
#         count+=1
