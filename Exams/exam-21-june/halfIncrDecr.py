
''''
1) Problem Statement: Rearrange the array such that the first half is arranged in increasing 
order, and the second half is arranged in decreasing order 
 
Test Cases: 
 
Example 1: 
Input: 8 7 1 6 5 9 
Output: 1 5 6 9 8 7 
Explanation: First three elements are in the ascending order and next three elements are in the 
descending order. 
 
Example 2: 
Input: 4 2 8 6 15 5 9 20 
Output: 2 4 5 6 20 15 9 8 

'''
nums=[int(i) for i in input().split() ]

nums=sorted(nums)
half=len(nums)//2

fst=sorted(nums[:half])
sec=sorted(nums[half:],reverse=True)

print(* fst+sec)



