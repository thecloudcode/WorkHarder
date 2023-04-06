def binpow(a,b):
    if b==0:
        return 1
    out_=binpow(a,b//2)
    out_=out_*out_

    if b%2!=0:
        out_=out_*a
    return out_

# print(binpow(2,3))
ans=0
n=int(input())
for i in range(1,n+1):
    ans+=binpow(2,i)
print(ans)
