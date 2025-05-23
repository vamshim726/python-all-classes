num = input()

sum=0
for i in num:
    sum= sum+int(i)

if int(num)%sum==0:
    print("harshad")
else:
    print("not harshad")