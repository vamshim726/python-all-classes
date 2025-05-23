n = int(input())

print("even numbers: ")
for i in range(1,n+1):
    if i%2 ==0:
        print(i,end=" ")
        
print()
print("odd numbers: ")
for i in range(1,n+1):
    if i%2 !=0:
        print(i,end=" ")
