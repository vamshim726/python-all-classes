# s=[[1,2,3],[4,5,6],[7,8,9]]

# s2=[]
# for i in s:
#     for j in i:
#         s2.append(j)
# print(s2)
# s = ['python', 'java', 'developer']

# for i in s:
#     for j in range(len(i)):
#         print(i[j])
#     print() # Add an empty line after each word


# s=['python','java','developer']
# for i in range(len(s)):
#     for j in range((s[i])):
#           print(j)



#print 1 to 10

# i=1
# while i<=10:
#     print(i)
#     i+=1


# -1 to -10


# i=-1
# while i>=-10:
#     print(i)
#     i-=1
      

# print using while
# s = ['python', 'java', 'developer']

# i=0
# while i<len(s): 
#     # print(s[i])
#     j=0
#     while j<len(s[i]):
#         # print(j)
#         print(s[i][j])
#         j+=1
#     print()
#     i+=1


#understand => s[0][0], s[0][1], s[0][2] so on
            #  s[1][0], s[1][0], s[1][2] so on



# print -10 to -1


# i=-10

# while i<=-1:
#     print(i)
#     i+=1





s=[2,3,4, 5,8,9]
# half decending, half ascending


half=len(s)//2

i=0
while i<=len(s):
    if i>half:
        print(s[-i]) 
    j=0
    if i<half:
        print(s[j+half])
        
    i+=1

