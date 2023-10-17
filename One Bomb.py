from collections import defaultdict
r=defaultdict(lambda:0)
c=defaultdict(lambda:0)
n,m = map(int,input().split())
x=[]
for _ in range(n):
    x.append(list(input()))
s=0

for i in range(n):
    for j in range(m):
        if x[i][j]=='*':
            s+=1
            r[i]+=1
            c[j]+=1

# print(dict(r),dict(c))
if n+m-1<s:
    print("NO")
elif s==0:
    print("YES")
    print(1,1)
else:
    flag=False
    ii=0
    jj=0
    for i in range(n):
        for j in range(m):
            # print(i,j,r[i],c[j])
            xxx=1 if x[i][j]=='*' else 0
            if r[i]+c[j]-xxx==s:
                flag=True
                ii=i
                jj=j
                break
        if flag:
            break
    if flag:
        print("YES")
        print(ii+1,jj+1)
    else:
        # print(s)
        print("NO")