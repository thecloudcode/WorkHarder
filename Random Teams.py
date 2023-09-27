import math

def nCr(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    else:
        return math.comb(n, r)

n,m=map(int,input().split())
maxx=n-(m-1)
minn=nCr((n//m)+1,2)*(n%m)+nCr(n//m,2)*(m-(n%m))
print(minn,nCr(maxx,2))

