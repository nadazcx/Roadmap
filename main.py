

numberOfshoes = input()
numberOfshoes = numberOfshoes.split(" ")
uniqueOnes=[]
for i in numberOfshoes:
    if i not in uniqueOnes:
        uniqueOnes.append(i)
print(4-len(uniqueOnes))
