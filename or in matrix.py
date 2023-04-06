n,m=map(int,input().split())
a=list(map(int,input().split()))
x=[]
xx=[]
f = False

for i in range(1,n+1):
    x.append(str(i))
    if i not in a:
        xx.append(' '.join(x[::-1]))
        x=[]
    if i==n:
        xx.append(' '.join(x[::-1]))
        x=[]
print(' '.join(xx))
