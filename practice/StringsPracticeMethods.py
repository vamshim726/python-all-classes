# str1= "    python    "
# print("Strip",str1.strip())  #removes starting and ending white spaces
# print("len",len(str1))    #returns length of string

# str2="python Is a interpreted language"
# print("capitalize",str2.capitalize())   # makes the first character uppercase and remeaing all to lowercase
# print("title",str2.title())   #converts each word's first character uppercase
# print("upper",str2.upper())   #converts entire string into uppercase
# print("lower",str2.lower())   #converts entire string into lowercase
# print("swapcase",str2.swapcase())   #it swaps the each case upper ones to lower, lower ones to upper
# print("index",str2.index("a"))   #it returns the first index of character
# print("count",str2.count("a"))   #it returns the number of charcters in string
# print("replace",str2.replace("a","z"))   #it replaces the first arg char with second arg character
# print("startswith",str2.startswith("P"))   #it return true if start with passed argment - case sensitive
# print("endswith",str2.endswith("e"))   #it return true if ends with passed argment


# str3="Thisispython"
# print("isalpha",str3.isalpha())   #it return true if it has only alphabets or single alphabet, returns false for all other charcters(spaces, nums,specalchars)

# str4="1234"
# print("isnumeric",str4.isnumeric())   #it return true if it has only numbers or single number,returns false for all other charcters(spaces, alphabets,specalchars) 

# str5="abc123"
# print("isalnum",str5.isalnum())   #it return true if it has only alphabets and numbers or single alphabet or nuumber, return false for all other chars 

# str6=" \n \t"
# print(str6.isspace())  #returns true for whitespace, newline escapeseq, tabspace escape sequence







# chatgpt ones below
 
str1 = "    python    "
print("Strip", str1.strip())  # Removes leading and trailing whitespace characters (spaces, tabs, newlines)
print("len", len(str1))       # Returns the total number of characters including whitespace

str2 = "python Is a interpreted language"
print("capitalize", str2.capitalize())  # Capitalizes first character and makes the rest lowercase
print("title", str2.title())            # Capitalizes the first letter of each word
print("upper", str2.upper())            # Converts all characters to uppercase
print("lower", str2.lower())            # Converts all characters to lowercase
print("swapcase", str2.swapcase())      # Swaps the case of each character
print("index", str2.index("a"))         # Returns the index of the first occurrence of "a"
print("count", str2.count("a"))         # Counts the total occurrences of "a" in the string
print("replace", str2.replace("a", "z"))# Replaces all occurrences of "a" with "z"
print("startswith", str2.startswith("P")) # Returns True if the string starts with "P" (case-sensitive)
print("endswith", str2.endswith("e"))     # Returns True if the string ends with "e"

str3 = "Thisispython"
print("isalpha", str3.isalpha())        # Returns True if all characters are alphabets only

str4 = "1234"
print("isnumeric", str4.isnumeric())    # Returns True if all characters are digits

str5 = "abc123"
print("isalnum", str5.isalnum())        # Returns True if all characters are alphabets or digits (no spaces/special chars)

str6 = " \n \t"
print(str6.isspace())                   # Returns True if the string contains only whitespace characters
