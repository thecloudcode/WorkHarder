n,m=map(int,input().split())
x=list(map(int,input().split()))
xx=x.copy()
minn=0
maxx=0
for i in range(n):
    maxx+=max(x)
    x[x.index(max(x))]-=1
    minn+=min(xx)
    if min(xx)==1:
        xx.remove(1)
    else:
        xx[xx.index(min(xx))]-=1
print(maxx,minn)
