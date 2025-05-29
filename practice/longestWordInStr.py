str1="The Microsoft Teams is a app".split()

maxLen=str1[0]
for i in str1:
    if len(i)+1>len(i):
        maxLen+=i
        
print(maxLen)