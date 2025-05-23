

#abcdefghij google microsoft


str1=[i for i in input().split()]

highestRepLetterWord=[]


for word in str1:
    maincounter=0

    for i in word:
        counter=0
        for j in word:
            if i==j:
                counter+=1
            