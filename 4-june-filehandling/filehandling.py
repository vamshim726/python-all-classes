
'''
    File Handling Modes

    1.read :  
    'r'
    read() : it reads file as a single string
    readline(): reads single line at a time
    readlines(): it reads each and evry line at a time


    2.write
    3.append
    4.binary


'''

file=open("studentData.txt",'r')

# content =file.read()
# print(content)

print("======================")



#readline

# line = file.readline()

# i=1
# while line:
#     print(f' line{i} :\n {line.strip()}')
#     line=file.readline()
#     i+=1


  


#readlines()

content = file.readlines() 

# print(content)

d1={}

for line in content:
    for word in line.strip().split():
        if word in d1:
            d1[word]+=1
        else:
            d1[word]=1
print(d1)

file.close()
# content2=file.readlines()
# print(content2)