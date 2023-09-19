numberOfWords=int(input())
L=[]
for i in range (numberOfWords):
    L.append(input())
    if (len(L[i])>10):
        L[i]=L[i][0]+str(len(L[i])-2) +L[i][-1]
for i in range(numberOfWords):
    print(L[i])