def binpow(a,b,m):
    a%=m
    res=1
    while(b>0):
        if :
            res=res*a%m
        a=a*a%m
        b/=2
    return res

d={'>':1000,'<':1001,'+':1010,'-':1011,'.':1100,',':1101,'[':1110,']':1111}
s=list(input())
ans=""
x=0
for i in s:
    ans+=str(d[i])
print(ans)
ans=ans[::-1]
for i in range(len(ans)):
    if ans[i]=='1':
        x+=binpow(2,i,1000003)
print(x)
