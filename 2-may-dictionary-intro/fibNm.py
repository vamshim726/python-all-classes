num=10

a,b=0,1
while a<=num:

    if a==num:
        print("fib")
        break 
    a,b=b,a+b
else:
        print("not fib")