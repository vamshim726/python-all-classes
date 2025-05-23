

# declaring dictionaries

d1={}

# or 

d2= dict()

#define dictionary
#type1

d3={"m1":80,"eng":90,"ed":88}

#type 2
d4=dict(India="delhi", usa="washington" , uk="london")
print(d3)
print(d4)


#accesing dictionary items
print(d3["m1"])
print(d3.get("eng"))

for i in d4:
    print(d4[i],end=" ")

#adding item in dictionary


#adding single element each time
d4["math"]=77
d4["webtech"]=68
print(d4)

# or 
# adding multiple elements in 1 time using update
d4.update({"telugu":50,"science":86})
print(d4)
