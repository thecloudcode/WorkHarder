n,k=map(int,input().split())

def cal(x,k,kk):
    if x//kk==0:
        return 0
    else:
        return x//kk + cal(x,k,kk*k)
# print(cal(7,2,2))

start=1
end=n
ans=n+1
while(start<=end):
    mid=(start+end)//2
    if cal(mid,k,k)+mid>=n:
        ans=min(ans,mid)
        end=mid-1
    else:
        start=mid+1
    # print(mid,ans)

print(ans)