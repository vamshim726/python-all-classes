#reverse list except last and first
l1 =input().split()
start,end = 1, len(l1) - 2

while start < end:
    temp = l1[start]
    l1[start] = l1[end]
    l1[end] = temp
    start += 1
    end -= 1

print(* l1)