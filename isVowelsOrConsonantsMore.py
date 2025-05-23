 
string = input("Enter a string : ")
vowelsCount =0
consonantCount =0
vowels="AEIOUaeiou"
for i in string:
    if i>="A" and i<="z" or i>="a" and i<="z":
        if i in vowels:
            vowelsCount+=1
        else:
          consonantCount+=1
if vowelsCount == consonantCount:
    print("Both are Equal")
elif vowelsCount > consonantCount:
    print("Vowels are more")
else:
    print("Consonants are more")
