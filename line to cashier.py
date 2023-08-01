n=int(input())
lol=list(map(int,input().split()))
ans=sum(list(map(int,input().split())))*5+15*lol[0]
for _ in range(n-1):
    ans=min(ans,sum(list(map(int,input().split())))*5+15*lol[_+1])
print(ans)

