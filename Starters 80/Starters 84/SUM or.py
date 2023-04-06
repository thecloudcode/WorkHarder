#Div 2 : SUM OR @codechef

mod=1000000007

def modpow(a,n,mod):
    a%=mod
    res=1
    while(n>0):
        if n&1 :
            res=(res*a)%mod
        a=(a*a)%mod
        n//=2
    return res



for _ in range(int(input())):
    n=int(input())
    b=str(bin(n))
    one=b.count('1')

    ans=modpow(3,one,mod)-3*modpow(2,one,mod)+3
    ans=(ans+3*mod)%mod
    print(ans)