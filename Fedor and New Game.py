n=int(input())
x=list(map(int,input().split()))
x.insert(0,0)
ans=0
for i in range(n):
    ans+=abs(x[i+1]-x[i])
print(ans)