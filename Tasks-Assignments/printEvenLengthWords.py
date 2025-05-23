

# WAP to print words with even lengths

# input: This is a python language
# output: This is python language


str1= input("Enter a String :").split()

for word in str1: 
    if len(word)%2==0:
        print(word, end=" ")