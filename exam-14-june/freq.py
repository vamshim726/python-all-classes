st=input()

st=st.replace(" ","")
st=sorted(st)
op=""
c=1
for i in range(1,len(st)):
    if st[i-1]==st[i]:
        c+=1
    else:
        op+=st[i-1]+str(c)+" "
        c=1
op+=st[-1]+str(c)
print(op)