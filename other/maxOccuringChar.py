

str1="thisisastring"  #a

checked=[]
counter=[]
for ch in str1:
    if ch not in checked:
        count=0
        for j in str1:
            if ch == j:
                count+=1
            checked.append(ch) 
        counter.append(count)

print(checked)
print(counter)
print(checked[counter.index(max(counter))])