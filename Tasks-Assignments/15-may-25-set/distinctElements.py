'''
Write program for the below problem using set and without set as well
Given an integer array arr[], print all distinct elements from this array. The given array may contain duplicates and the output should contain every element only once.

Examples: 

    Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
    Output: {12, 10, 9, 45, 2}

    Input: arr[] = {1, 2, 3, 4, 5}
    Output: {1, 2, 3, 4, 5}

    Input: arr[] = {1, 1, 1, 1, 1}
    Output: {1}


'''

#approach 1

def distinct1():

    set1=[int(i) for i in input().split()]
    distinct=set(set1)
    print(* distinct)


#approach2

def distinct2():
    set2=[int(i) for i in input().split()]
    distinct=[]
     
    for i in set2:
        if i not in distinct:
            distinct.append(i)
            print(i,end=" ")

distinct1()
distinct2()