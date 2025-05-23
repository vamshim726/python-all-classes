str1=input()

vowels="aeiouAEIOU"
count=0

for i in str1:
    if i in vowels:
        print(i,end=" ")
        count+=1

print(count)