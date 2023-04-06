n=int(input())
x=list(map(int,input().split()))
minn=abs(x[-1]-x[0])
a=n
b=1
for i in range(n-1):
    if abs(x[i+1]-x[i])<minn:
        a=i+1
        b=i+2
        minn=abs(x[i+1]-x[i])
print(a,b)