

num1 = int(input())
num2 = int(input())

res = num1 if num1>num2 else num2

while True:
    if res%num1 == 0 and res%num2==0:
        print(f"The LCM of {num1} and {num2} is: {res}")
        break
    else:
        res+=1
