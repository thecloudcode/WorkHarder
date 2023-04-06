N=int(input())
xx=[]
x=[]
for i in range(N):
    for j in range(N):
        x.append(int(input()))
    xx.append(x)
    x=[]
y=[]
yy=[]
for i in range(N):
    for j in range(N):
        y.append(xx[i][j])
    print(y)
    y=[]
d={}
for i in range(N):
    for j in range(N):
        y.append(xx[j][i])
        d[xx[j][i]]=xx[i][j]+1
    print(y)
    y=[]
print(d)