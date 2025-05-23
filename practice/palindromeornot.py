# str1=input()

# res=""

# for i in range(len(str1)-1,-1,-1):
#     res=res+str1[i]

# if res==str1:
#     print("palindrome")
# else:
#     print("not palind")


# or 

# using slicing

str1=input()
print("palindrome") if str1[::-1]== str1 else print("Not palindrome")