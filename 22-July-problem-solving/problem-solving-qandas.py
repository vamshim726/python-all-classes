
'''is arr1 is subset of arr2'''


arr1=[1,3,4,5,2]
arr2=[2,4,3,1,7,5,15,15]

#approach 1

def isSubset1(arr1,arr2):

    if len(arr2)<len(arr1):
        return False

    flag=True
    for i in arr1:
        if i not in arr2:
            flag=False
    return flag


#approach 2 using inbuilt method
#issubset()


def isSubset2(arr1,arr2):

    return set(arr1).issubset(set(arr2))
    

print(set(arr1))
print(set(arr2))

print('arr1 is subset of arr2' if isSubset2(arr1,arr2) else 'arr1 is not a subset of arr2')
