# #Print missing  fibonacci numbers till given num

# num= int(input())

# a,b=0,1
# nonFib=0

# while nonFib!=num:
#     for i in range(a+1,b):
#         if nonFib==num:
#             break
#         nonFib+=1
#         print(i,end=" ")
    
#     a,b=b,a+b







num=int(input())

fibNumbers=[]

a,b=0,1

while a<=num:
    fibNumbers.append(a)
    a,b=b,a+b


for i in range(0,num):

    if i not in fibNumbers:
        print(i,end=" ")

# print(fibNumbers)