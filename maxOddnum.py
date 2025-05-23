# 1)
# Problem statement: Program to print maximum odd digit in the given number

# Test Case-1:
# input: Enter a number: 5788
# output: 7 is the max odd 

# Test Case-2:
# input: Enter a number: 680
# output: There is no odd numbers



num = input()
maxOdd= float('-inf')
for i in num:
    if i>='0' and i<='9':
        if int(i)%2!=0 and int(i)>maxOdd:
            maxOdd=int(i)
    
print("There is no odd numbers") if maxOdd==float('-inf') else print(f"{maxOdd} is the max odd ")