

# def isValidPass(s1,n):

#     cap,num=0,0
#     if n < 4:
#         return 0
    
#     if s1[0].isdigit():
#         return 0
#     for i in range(len(s1)):
#         if s1[i]==" " or s1[i]=="/":
#             return 0
#         if s1[i] >="A" and s1[i]<="Z" :
#             cap+=1
#         elif s1[i].isdigit():
#             num+=1
#     if cap>0 and num>0:
#         return 1
#     else:
#         return 0
            






def isValid2(pw,n):
    if n<4 or " " in pw or "/" in pw or (pw[0]>="0" and pw[0]<="9"):
        return 0
    else:
        num,cap=0,0
        for i in pw:
            if i.isdigit():
                num+=1
            elif i.isupper():
                cap+=1
        if cap>0 and num>0:
            return 1
        else:
            return 0
s1="aA1_67"
n=len(s1)
# print(isValidPass(s1,n))
print(isValid2(s1,len(s1)))
