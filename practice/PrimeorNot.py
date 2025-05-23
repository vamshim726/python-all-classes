num=int(input())

if num>1:
    for i in range(2,(num//2)+1):
        if num%i==0:
            print(f"{num} is Not Prime ")
            break
    else:
        print("Number is Prime")
else:
    print("Enter a valid Number")