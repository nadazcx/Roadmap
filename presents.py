n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    print(i)
    l1[i] = l.index(i+1)
print(l1)