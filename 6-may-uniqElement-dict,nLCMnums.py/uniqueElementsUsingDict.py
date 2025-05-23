words = [i for i in input("Enter string: ")]

uniq = ""
dup = ""

d1 = {}

for word in words:
    if word not in d1:
        d1[word] = 1
    else:
        d1[word] += 1

for word in d1:
    if d1[word] == 1:
        uniq += word + " "
    else:
        dup += word + " "

print("Unique words:")
print(uniq.strip())

print("-----")

print("Duplicate words:")
print(dup.strip())
