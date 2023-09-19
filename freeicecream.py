user_input = input().split()
listNumber = list(map(int, user_input))
distressed=0

for i in range(listNumber[0]):
    x=input()
    addons=int(x[1::])
    if x[0]== "+":
        listNumber[1]+=addons
    if x[0]== "-":
        if listNumber[1]>=addons:
            listNumber[1]-=addons
        else:
            distressed+=1
print(str(listNumber[1])+" "+str(distressed))

