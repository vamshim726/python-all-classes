

num=int(input()) #12345
orgNum=num

rev=0

while num !=0:
    rem=num%10
    rev=10*rev+rem
    num//=10

print("Reversed Number is :",rev)

