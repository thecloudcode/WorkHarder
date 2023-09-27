from bisect import bisect_right
n,m=map(int,input().split())
x=sorted(list(map(int,input().split())))
xx=list(map(int,input().split()))

c=[]
for i in xx:
    c.append(bisect_right(x,i))
for i in c:
    print(i,end=" ")