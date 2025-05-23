

list1= [1,2,9,7,5,6]
 
 
s=0
e=len(list1)-1

while s<e:
    list1[s],list1[e]=list1[e],list1[s]
    s+=1
    e-=1


print(list1)
