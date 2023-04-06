from collections import defaultdict

n=int(input())
x=sorted(list(map(int,input().split())))

c=defaultdict(lambda:0)
flag=True
one=0
two=0
for i in x:
    c[i]+=1
    if c[i]>=3:
        flag=False
        break
    if c[i]==1:
        one+=1
    if c[i]==2:
        one-=1
        two+=1


if flag:
    inc=""
    dec=""
    for i in range(n):
        if c[x[i]]==2:
            c[x[i]]-=1
            inc+=str(x[i])+" "
    for i in range(n):
        ii=n-i-1
        if c[x[ii]]==1:
            c[x[ii]]-=1
            dec+=str(x[ii])+" "
if flag:
    print("YES")
    print(len(inc)//2)
    print(inc[:-1:])
    print(len(dec)//2)
    print(dec[:-1:])
else:
    print("NO")