n,x=map(int,input().split())
a,b=map(int,input().split())
if b>x:
    ans=a-(b-x)
else:
    ans=a
for _ in range(n-1):
    a, b = map(int, input().split())
    if b>x:
        ans=max(ans,a-(b-x))
    else:
        ans=max(ans,a)
print(ans)