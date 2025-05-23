# https://takeuforward.org/data-structure/check-if-the-given-number-is-harshador-niven-number/

num = input()

sum=0
for i in num:
    sum+=int(i)

if int(num)%sum==0:
    print("Yes it is a Harshad number.")
else:
    print("No it is not a Harshad number.")

 