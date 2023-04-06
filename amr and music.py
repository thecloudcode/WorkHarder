n,k=map(int,input().split())
x=list(map(int,input().split()))
a=sorted(x)
s=[]
ss=[]
c=0
for i in range(len(a)):
    if sum(ss)+a[i]<=k:
        s.append(x.index(a[i])+1)
        ss.append(a[i])
        x.insert(x.index(a[i]),-1)
        x.remove(a[i])
        c+=1
    else:
        break
print(c)
x=[str(i) for i in s]
if len(x)>0:print(' '.join(x))
