


arr=[2,5,7,1,3,6,9,4]
k=4

def rotateByKRight(arr,k):
    res=[]
    steps= k%len(arr)
    for i in range(steps,len(arr)):
        res.append(arr[i])
    
    res.extend(arr[:k])

    return res

print(rotateByKRight(arr,k))
