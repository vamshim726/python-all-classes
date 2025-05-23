'''
2) Python program to find the sum of all items in a dictionary

input: {'a': 100, 'b': 200, 'c': 300}

output: 600

'''


d1= {'a': 100, 'b': 200, 'c': 300}

sum=0
for val in d1.values():
    sum+=val

print(sum) 