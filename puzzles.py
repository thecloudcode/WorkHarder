n,m=map(int,input().split())
x=sorted(list(map(int,input().split())))
# print(x)
ans=max(x)
for i in range(m-n+1):
    # print(x[i+3],x[i])
    ans=min(ans,abs(x[i+n-1]-x[i]))
print(ans)