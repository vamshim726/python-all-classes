


# F 


n=5

# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n//2:
#             print('*',end=' ')
            # else:
            #     print('  ',end="")
#     print()



# h 

for i in range(n):
    for j in range(n):
        if j==n-1 or j==0 or i==n//2:
            print('*',end=' ')
        else:
            print('  ',end="")
    print()