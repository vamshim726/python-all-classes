
# palindromes in given range 

# n1,n2=[int(i) for i in input().split()]

# pal=[]
# for i in range(n1,n2+1):

#     if str(i)==str(i)[::-1]:
#         pal.append(i)

# print(* pal)


#exams 

t= int(input())

for i in range(t):
    x,y,z=[int(i) for i in input().split()]
    ts=x*y
    print("Yes" if (z/ts)*100>50 else "No")