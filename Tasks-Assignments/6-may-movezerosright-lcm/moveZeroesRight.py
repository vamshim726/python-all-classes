'''
1) Program to rearrange all the non zeroes to the starting of the list and zeroes to the end of list

input: 10 5 0 30 0
output: 10 5 30 0 0


'''


nums=[int(i) for i in input().split()]

nonZeroes=[i for i in nums if i>0] 
zeroes=[i for i in nums if i==0]

print(* nonZeroes+zeroes)