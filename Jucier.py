n,b,d = map(int,input().split())
x=list(map(int,input().split()))

c=0
dd=0

for i in x:
    if i<=b:
        if dd<=d and dd+i>d:
            c+=1
            dd=0
        else:
            dd+=i

print(c)