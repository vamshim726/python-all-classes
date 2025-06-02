s='this is an amazing program'.split()
rev=[]
for i in s[::-1]:
    rev.append(i)

print(* rev)


#appraoch 2

s2='this is an amazing program'

rev=""
for i in range(len(s2)-1,-1,-1):
    if s2[i]==" ":
        print(f"{rev}",end=" ")
        rev=""
    else:
        rev=s2[i]+rev
print(rev)