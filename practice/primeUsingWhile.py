num=11

i=2
while(i<(num//2)+1):
    if num%i==0:
        print("no prime")
        break
    i+=1
else:
    print("prime")


# for i in range(2,(num//2)+1):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")