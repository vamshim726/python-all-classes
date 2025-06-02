#zip : it converts the iterables to tuple of list

# syntax: 

#zip(*iterable)

#same length

nums=[1,3,4,7,8,9]
strs="vamshi"

print(* zip(nums,strs))
# it returns a tuple


res=list(zip(nums,strs))
print(res)


#single iterable
nums2=[10,20,30,40]
print(list(zip(nums2)))


#different length - it takes smallest iterable

str2="hellohi"
nums3={1:5,6:7,8:2}
print(list(zip(str2,nums3)))


#unziping

res=[("google",2),("amazon",5),("ibm",5)]
companies,nums4=zip(*res)
print(companies)
print(nums4)
