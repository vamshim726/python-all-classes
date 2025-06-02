'''
    asked on 31 may 2025

'''

words=["abc","abbgv","ab"]

# for i in range(0,len(words)):
#     for j in range (i+1,len(words)):
#         if len(words[i])>len(words[j]):
#             words[i],words[j]=words[j],words[i]

# print(words)



s1=["abc","abbgv","ab"]
 
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if len(s1[i])>len(s1[j]):
            s1[i],s1[j]=s1[j],s1[i]
            
            
print(s1) 