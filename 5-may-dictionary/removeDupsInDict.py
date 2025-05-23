
d1={"gfg":20,"is":10,"very":20,"good":15,"platform":10}


res={} #or res= dict()
unique=[]

for i in d1 :
    val=d1[i]
    if val not in unique:
        unique.append(val)
        res[i]=val


print(unique)