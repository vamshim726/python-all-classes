# Date: 16 April 2025



str1= input("Enter a String : ") 
for i in range(len(str1)):
    if i==0 or i==len(str1)-1 or str1[i+1] ==" " or  str1[i-1]==" " :
        print(str1[i].upper(),end="")
    else:
        print(str1[i],end="")
