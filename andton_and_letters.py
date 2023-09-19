

theLetters =input()
theLetters=theLetters[1::]
theLetters=theLetters[:-1]
theLetters=theLetters.split(", ")
uniques=[]
for i in theLetters:
    if i not in uniques:
        uniques.append(i)
#print(uniques)
if uniques==[''] :
    print("0")
else :
    print(len(uniques))