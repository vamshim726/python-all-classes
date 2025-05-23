
num = int(input("Enter a number : "))
result = ("Negitive number"    if num < 0 else 
         "Single digit number" if num >=0 and num < 10 else 
         "two digit number"    if num >=10 and num< 100 else
         "three digit number"  if num >=100 and num< 1000 else
         "More than three digits"
         
         )
print(result)