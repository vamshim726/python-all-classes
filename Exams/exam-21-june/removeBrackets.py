
''' 

2) Problem Statement: Remove brackets from an algebraic expression 
 
Write a program to remove brackets from an algebraic expression 
 
Given an algebraic expression, we need to simplify the expression and remove the brackets. 
 
Test Cases: 
 
Example 1: 
Input: “a+((b-c)+d)” 
Output: “a+b-c+d” 
Explanation: Removed all the brackets in the algebric expression. 
 
Example 2: 
Input: “(((a-b))+c)” 
Output: “a-b+c” 
Explanation: Removed all the brackets in the algebric expression. 
'''

exp=input()
out=""

for i in exp:
    if i!="(" and i!=")":
        out+=i 

print(out)

