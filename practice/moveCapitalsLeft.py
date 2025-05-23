# input: Great Learning
# Output: GLreatearning


str1="Great Learning"

caps=""
smalls=""


for i in range(len(str1)):
    if str1[i]>="A" and str1[i]<="Z":
        caps+=str1[i] 
    else:
        if str1[i]!=" ":
            smalls+=str1[i]
print(caps+smalls)

