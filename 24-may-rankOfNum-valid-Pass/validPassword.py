


'''
You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:
Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0


'''

def isValidPass(pw,n):
    cap,dig=0,0
    if len(password)<4 or " " in password or "/" in password or password[0].isdigit() :
        return 0
    for i in pw:
        if i.isupper():
            cap+=1
        elif i.isdigit():
            dig+=1
    if cap>0 and dig>0:
        return 1

password=input()
print(isValidPass(password,len(password)))