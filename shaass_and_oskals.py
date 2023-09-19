n = int(input())
y= input()
wires= y.split(" ")
for i in range(len(wires)):
    wires[i]= int(wires[i])
m=int(input())
for i in range(m) :
    z= input()
    z=z.split(" ")
    x1=int(z[0])
    y1=int(z[1])
    if(x1+1<=n):
        wires[x1]=wires[x1-1]-y1+wires[x1]
    if(x1-1>=1) :
        wires[x1-2]=y1-1+wires[x1-2]
    wires[x1-1]=0
for i in range(n) :
    print(wires[i])
