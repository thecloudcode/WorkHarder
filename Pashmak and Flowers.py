n=int(input())
x=list(map(int,input().split()))

maxx=x.count(max(x))
minn=x.count(min(x))
if max(x)!=min(x):
    print(max(x)-min(x),minn*maxx)
else:
    print(0,int(n*(n-1)/2))