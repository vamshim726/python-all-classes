
#common prefix second logic

strs=["flower","flow","flight"]


out=""
# print(list(zip(*strs)))
res= list(zip(*strs))
for i in res:
    if len(set(i))==1:
        out+=i[0]
    else:     # it reduce some iterations
        break
# print(out)

print(out if out else "There is no common prefix")