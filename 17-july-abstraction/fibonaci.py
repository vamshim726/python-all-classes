from traceback import print_tb

a=0
b=1
n=int(input('enter range to print fibonoci series:'))
print(f'first {n} fibonoci series')
for i in range(n):
    print(a)
    # c=a+b
    # a=b
    # b=c
    a,b=b,a+b
