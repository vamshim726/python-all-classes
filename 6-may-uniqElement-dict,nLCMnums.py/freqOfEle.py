
s=[2, 3, 2, 5, 4, 8, 4, 5, 1, 7]

freq=[""]*len(s)

for i in range(len(s)):
    c=0
    if freq[i]!=-1:
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                c+=1
                freq[j]=-1
    if freq[i]!=-1:
        freq[i]=c+1
print(freq)

for i in range(len(s)):
    if freq[i]!=-1:
        print(s[i],freq[i])