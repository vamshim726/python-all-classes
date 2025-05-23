# #0
# for i in range(0,10+1):
#     print(i,end=" ")

# print()
# #1
# for i in range(-10,0):
#     print(i,end=" ")
# print()

# #2
# for i in range(-10,0,2):
#     print(i,end=" ")

# print()

# #3
# for i in range(-1,-21,-1):
#     print(i,end=" ")


# print()

# #print even and odd
# #way1
# even=[]
# odd=[]
# for i in range(10,21):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(* even)
# print(* odd)

# # way2
# print("evens")
# for i in range(10,21,2):
#     print(i,end=" ")

# print()
# print("odds")
# for i in range(11,21,2):
#     print(i,end=" ")





# #5
# print("list")
# print("list")
# print("list")
# print("list")
# s=[1,2,3,4,4,4,5,6,5]
# s.pop()
# s.remove(1) 
# s.sort()
# s.insert(0,9)
# s.count(4)
# s.append([11,11,111])
# s.extend([10,20])

# print(s)
# s.clear()




# # reverse string 
# #way 1
# s1="python"
# rev=""

# for ch in s1:
#     rev=ch+rev 
# print(rev)

# #way2
# print(s1[::-1])


# #way3
# rev="".join(reversed(s1))
# print(rev)

# #way4
# rev=""
# for i in range(len(s1)-1, -1, -1):
#     rev += s1[i]
# print(rev)



           
# print()
# print()
# print()
# print()

# #multiply even indexes with 2 and add to same list with same index


# print("multiply with for even nums")
# p=[1,2,3,4,5,6,7,8,9]

 
# for i in range(len(p)):
#     if p[i]%2==0:
#         p[i]=p[i]*2

# print(p)
 





# # multiply*2 for int datatype at even index
# lst3=[1,2,3,True,4,5,6,"hi"]

# for i in range(len(lst3)):
#     if type(lst3[i])==int and p[i]%2==0:
#         lst3[i]=lst3[i]*2 
# print(lst3)


# #print 10 to 20 tables

# # for nums in range(10,21):

# #     for i in range(1,11):
# #         print(f"{nums}*{i}={i*nums}") 
# #     print()




# #if leap year give 20% discout else 10% discount

# # price=int(input("Enter Price : "))
# # year=int(input("Enter purchased year : "))

# # #leap year
# # if ( year%4==0 and year%100!=0) or year%400==0:
# #     print(f"Your Total Bill is {price-(price*20)/100}")
# # #non leap year
# # else: 
# #     print(f"Your Total Bill is {price-(price*10)/100}")




# #ascending order without sort method
numslist=[5,2,8,9,1,3]


for i in range(len(numslist)):
    for j in range(i+1,len(numslist)):
        if numslist[j]<numslist[i]:
            temp=numslist[i]
            numslist[i]=numslist[j]
            numslist[j]=temp

print("after sorting",numslist)




# numlist=[4,7,2,9,66,33,77,8,2]
# max=float('-inf')
# for num in numlist:
#     if num>max:
#         max=num

# print("max num is",max)


list1=[[5,6,8],[6,2,1],[5,3,2]]

maxNumsStr=""

for sublist in list1:
    
    maxnum=0
    for num in sublist:
        if num>maxnum:
            maxnum=num
    maxNumsStr+=str(maxnum)

print(* maxNumsStr)














