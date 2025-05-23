

num=121

org_no=num

rev_no=0

while num!=0:
    ld=num%10
    rev_no=rev_no*10+ld
    num=num//10

if org_no==rev_no:
    print("palindrome")

else:
    print("not palindrom")

'''
    num=1
    rev=12

    ld=2
    rev=12
    num=1




'''