

def findUniqNum(nums):

    d1=dict()
    uniq=""
    for i in nums: 
        if i not in d1:
                d1[i]=1
        else:
                d1[i]+=1

                
    for key in d1:
          if d1[key]==1:
            uniq+=str(key)
    if not uniq:
         return "No uniq num found"
    
    return uniq

nums=[2, 2, 2, 3, 4, 4, 4]
print(findUniqNum(nums))