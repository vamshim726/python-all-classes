#ab[13]c[10]  => ababababa 13 times   cccc 10 times
#20011 -> 11200  move odd at first place
#2518 -> 5182

# s="ab[13]c[10]"
# s="a[2]b[3]"
s="[3]ab[10]c"

ch=""
n=""
for i in s:
    if i !="[" and i !="]" and not i.isdigit() :
        ch+=i
    elif i.isdigit():
        n+=i
    if i=="]":
        ch+="," 
        n+=","
ch=ch.strip(',').split(',')
n=n.strip(',').split(',')

for i in range(len(ch)):
    print(ch[i]*int(n[i]))

print(ch,n)