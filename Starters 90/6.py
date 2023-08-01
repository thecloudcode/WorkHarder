
from collections import defaultdict
import math

mod = 10**9 + 7
MX = 100005
fac = [1]
invfac = [1]
for i in range(1, MX):
	fac.append(i * fac[i-1] % mod)
	invfac.append(pow(fac[-1], mod-2, mod))
def C(n, r):
	if n < r or r < 0: return 0
	return fac[n] * invfac[r] % mod * invfac[n-r] % mod



for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    # a,b=map(int,input().split())
    # s=input()
    # d=defaultdict(lambda:0)
    ans=0
    for i in range(n):
        rt=pow(2,n-i-1,mod)
        lt=C(i,a[i]-1)
        ans+=lt*rt%mod
    print(ans%mod)