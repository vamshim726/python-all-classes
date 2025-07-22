

def add(a,b):
    return a + b

def add(a,b,c):
    return a+b+c

def add(a,b,c,d):
    return a+b+c+d

# add(3,4)
# add(3,4,5)
# print(add(3,4,5,6))



#method overdinig achieved using arbitary, keyword arbitory arguments


def add(*nums):

    res=0

    for i in nums:
        res+=i
    return res

print(add(10,10,10,10,10,10))


