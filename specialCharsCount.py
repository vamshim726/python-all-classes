# 2) 
# Problem statement: Program to print count of special characters in the given string

# Test Case-1:
# input: Welcome@John!
# output: @1 

# Test Case-2:
# input: support@gmail.com
# output: @.


str1= input()
for i in str1:
    if not (i>="a" and i<="z" or i>"A" and i<"Z" or i >="0" and i<="9"):
        print(i,end="")
        