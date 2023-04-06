n,k,l,c,d,p,nl,np=map(int,input().split())
ll=k*l
dd=c*d
print(min(ll//nl,dd,p//np)//n)