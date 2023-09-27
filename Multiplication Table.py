n=int(input())
a=[]
x=[]
for i in range(n):
    xx=list(map(int,input().split()))
    x.append(xx)
azero=int((x[0][1]*x[0][2]/x[1][2])**0.5)
a.append(azero)
# print(azero)
ind=1
while(ind<n):
    a.append(int(x[ind][ind-1]/a[-1]))
    ind+=1
for i in a:
    print(i,end=" ")
