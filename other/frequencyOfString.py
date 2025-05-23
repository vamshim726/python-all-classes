# # https://takeuforward.org/data-structure/calculate-frequency-of-characters-in-a-string/


str1 = "zabca" #input() #articlesa    => a2 c1 e1 i1 l1 r1 s1 t1


checked=""
for i in range(len(str1)):
    char= str1[i]
    if char not in checked:
        count=0
        for j in range(len(str1)):
            if str1[j]==char:
                count+=1
        print(f"{char}{count}",end="")
        checked+=char
            

         

# str1 = "abca" #input() #articlesa    => a2 c1 e1 i1 l1 r1 s1 t1



# str1=input()

# freqstr=""
# checked=""

# for ch in str1:
#     if ch not in checked:
#         count=0
#         for j in range(len(str1)):
#             if str1[j]==ch:
#                 count+=1
#         checked=checked+ch
#         freqstr=freqstr+ch+str(count)

# print(freqstr)
        











# str1="takeuforward"

# str1=sorted(str1)
# str1="".join(str1)
# print(str1)


# freqstr=""
# checked=""

# for ch in str1:
#     if ch not in checked:
#         count=0
#         for j in range(len(str1)):
#             if str1[j]==ch:
#                 count+=1
#         freqstr+=ch+str(count)+" "
#         checked+=ch

# print(freqstr)