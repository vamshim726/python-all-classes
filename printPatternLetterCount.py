str1=input()
i=1
for ch in str1:
    if ch >="a" and ch<"z" or ch>="A" and ch<="Z":
        print(f"{ch}{i}",end="")
        i=i+1