
# WAP to print all the uppercase letters first followed by lowercase letters in the given string

# input: Great Learning
# Output: GLreatearning




str1=input("Enter a String: ")
capital=""
small=""

for i in str1:
    if i>="A" and i<="Z":
        capital+=i
    elif i>="a" and i<="z":
        small+=i


print(capital+small)