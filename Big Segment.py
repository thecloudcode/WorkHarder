n=int(input())
mina,maxb=map(int,input().split())
x=[[mina,maxb]]
for i in range(n-1):
    a,b=map(int,input().split())
    mina=min(a,mina)
    maxb=max(b,maxb)
    x.append([a,b])
f=True
for i in range(n):
    if x[i][0]==mina and x[i][1]==maxb:
        print(i+1)
        f=False
        break
if f:
    print(-1)

