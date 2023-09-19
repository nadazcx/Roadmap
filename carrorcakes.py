import math

buf=list(map(int,input().split(" ")))
n=buf[0]
t=buf[1]
k=buf[2]
d=buf[3]
rounds=math.ceil((n/k))
timeO1=rounds*t
o1=t
o2=d
#print(rounds)
for i in range(int(rounds-1)):
    if (o1<=o2):
        o1+=t
    else:
     o2+=t
#print("o2",o2,"o1",o1,"time 01",timeO1)
L=[o1,o2]
L=max(L)
if (L<timeO1):
    print("YES")
else:
    print("NO")