s=input()
m="+1"*s.count("1")+"+2"*s.count("2")+"+3"*s.count("3")
if m!="":
    m=m[1::]
print(m)