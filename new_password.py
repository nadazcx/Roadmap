L=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x=list(map(int,input().split(" ")))
length=x[0]
distinct=x[1]
print((("".join(L[:distinct]))* (length//distinct)) + "".join(L[:length%distinct]))