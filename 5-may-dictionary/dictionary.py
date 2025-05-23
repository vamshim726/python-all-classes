subjects_marks={"m1":90,"eng":33,"phy":90,"c":86}

marks=subjects_marks.values()
maxMarks=max(marks)
minMarks=min(marks)

maxlist=[]
minlist=[]

#print subjects of and min marks
for i in subjects_marks:
    if subjects_marks[i]==maxMarks:
        # print("max is",i)
        maxlist.append(i)
    elif subjects_marks[i]==minMarks:
        # print("min is",i)
        minlist.append(i)
print("list with max marks", * maxlist)
print("list with min marks", * minlist)
    


# for x,y in subjects_marks.items():
#     print(x,y)