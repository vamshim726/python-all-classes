'''
1) WAP to print the dictionary items in which the the key starts with a letter 't'

input: The original dictionary : {'tough': 1, 'to': 2, 'do': 3, 'todays': 4, 'work': 5}

Output:
Filtered dictionary keys are : {'tough': 1, 'to': 2, 'todays': 4}


'''

d1=dict()

n= int(input("Enter dictionary size : "))

for _ in range(n):
    key=input("enter key : ")
    value=int(input("enter value : "))
    d1[key]=value

d2={}

for x,y in d1.items():
    if x[0]=="t":
        d2[x]=y
print(d2)