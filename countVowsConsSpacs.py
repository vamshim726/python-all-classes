
str1= input("Enter a string: ")
vowels ="aeiouAEIOU"
vowelsCount,consonantsCount,spacesCount=0,0,0
for i in str1:
    if i == " ":
        spacesCount+=1
    elif i in vowels:
        vowelsCount+=1
    else:
        consonantsCount+=1

print(f"""Vowels: {vowelsCount}
Consonants: {consonantsCount}
Whitespaces: {spacesCount}""")
