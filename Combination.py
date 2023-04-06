n=int(input())
x=[]
ans=0
check=1
for i in range(n):
    a,b=map(int,input().split())
    if b>=1:
        ans+=a
        check+=b-1
    else:
        x.append(a)
x.sort()
x=x[::-1]

for i in range(min(len(x),check)):
    ans+=x[i]
print(ans)