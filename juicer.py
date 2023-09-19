n = input()
n = n.split(" ")
a = input()
a = a.split(" ")
bin = 0
times = 0
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(n)):
    n[i] = int(n[i])
for i in range(n[0]):

    if (a[i] <= n[1]):
        bin += a[i]
    if (bin > n[2]):
        bin = 0
        times += 1

print(times)