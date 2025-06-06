


str1="abp50cd856sdf75"



def findLargestNumInStr(s):
    
    num=""
    maxNo=float('-inf')

    for i in s:

        if i>="0" and i<="9":
            num+=i
        elif num:
            num=int(num)
            if num>maxNo:
                maxNo=num
            num=""
    if num:
        if int(num)>maxNo:
            maxNo=int(num)

    return maxNo

print(findLargestNumInStr(str1))