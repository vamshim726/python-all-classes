

str1=input()  #MCMXCIV


def romanToInteger(str1):
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    prev=0
    total=0
    for cr in str1[::-1]:
        value=roman[cr]
        if value>=prev:
            total+=roman[cr]
        else:
            total-=value
        prev=value

    return total

print(romanToInteger(str1))