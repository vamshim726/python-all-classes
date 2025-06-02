

def findMissing(lst):
    maxnum=max(lst)    
    minnum=min(lst) 
    missing=[]
    for i in range(minnum+1,maxnum):
        if i not in lst:
            missing.append(i)
    return missing

nums=[2,3,5,6,7,9]
print(findMissing(nums))