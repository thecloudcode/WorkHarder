n,xx=map(int,input().split())
x=xx
aa=[]
bb=[]
for i in range(n):
    a,b=map(int,input().split())
    aa.append(a)
    bb.append(b)
    if(x>=min(a,b) and x<=max(a,b)):
        continue
    else:
        if(x>max(a,b)):
            x=max(a,b)
        elif(x<min(a,b)):
            x=min(a,b)

flag=True
for i,j in zip(aa,bb):
    if x>=min(i,j) and x<=max(i,j):
        continue
    else:
        flag=False
        break
print(abs(x-xx) if flag else -1)
