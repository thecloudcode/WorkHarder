n,a,b,c,d=map(int,input().split())
x=list(input())

go=""
if c>a:
    go+="E"
elif c<a:
    go+="W"
if d>b:
    go+="N"
elif d<b:
    go+="S"
# print(go)
xx=c
yy=d
c=0

for i in range(len(x)):
    if xx==0 and yy==0:
        break
    if x[i] in go:
        if x[i]=='N' and yy!=b:
            yy-=1
            c=i+1
        if x[i]=='S' and yy!=b:
            yy+=1
            c=i+1
        if x[i]=='W' and xx!=a:
            xx+=1
            c=i+1
        if x[i]=='E' and xx!=a:
            xx-=1
            c=i+1
    # print(xx, yy)

print(c if xx==a and yy==b else -1)
