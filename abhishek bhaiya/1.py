s=list(input())
x=list(input())

c=0
for i in s:
    if i in x:
        c+=1

if c<2:
    print(2)
elif c>=2 and c<5:
    print()