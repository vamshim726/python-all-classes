# Write a program to remove all characters from a string except alphabets in a given string.

# Examples:

# Example 1:
# Input: string str = "take12% *&u ^$#forward"
# Output: takeuforward
# Explanation:
# Characters 1,2,%,*,&,^,$,# along with whitespaces are 
# removed but the order of remaining alphabets is preserved.

# Example 2:
# Input: String str = "1.Python & 2.Java"
# Output: PythonJava
# Explanation: 
# Characters 1.&2. along with whitespaces are removed 
# but the order of remaining alphabets is preserved.
 

str1 = input()
for i in str1:
    if i>="a" and i<="z" or i>="A" and i<="Z":
        print(i,end="")
        
