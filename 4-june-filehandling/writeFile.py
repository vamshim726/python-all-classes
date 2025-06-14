data =["vamshi 22","rahu 23", "jhon 24"]

 
file =open('studentData.txt','w')


for i in data:
    file.write(i+'\n')

file.write('............')

# fil=open('studentData.txt','w')
# fil.write("....")