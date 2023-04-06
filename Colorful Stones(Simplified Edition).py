s=list(input())
t=list(input())

c=1
for i in t:
    if i==s[c-1]:
        c+=1
print(c)