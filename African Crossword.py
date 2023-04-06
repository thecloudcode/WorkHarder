a,b=map(int,input().split())
x=[]
xx=[]
for i in range(a):
    lol=list(input())
    x.append(lol)
    xx.append(lol.copy())
for i in range(a):
    for j in range(b):
        for k in range(j+1,b):
            # print(xx[i],x[i])
            # print(xx[j],x[j])
            if xx[i][j]==xx[i][k]:
                x[i][j]='aa'
                x[i][k]='aa'
        for k in range(i+1,a):
            if xx[i][j]==xx[k][j]:
                x[i][j]='aa'
                x[k][j]='aa'
ans=""
for i in range(a):
    for j in range(b):
        if x[i][j]!='aa':
            ans+=x[i][j]
print(ans)