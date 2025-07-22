

n=[1,2,4,5,7,7,5]

small=float('inf')
secSmall=float('inf')
for i in range(len(n)):
    if (n[i]<small):
        secSmall=small
        small=n[i]
    elif n[i]<secSmall and n[i]!=small:
        secSmall=n[i]

print(secSmall)  