n,k=map(int,input().split())
x=list(map(int,input().split()))
print(-1 if (n-1)*10+sum(x)>k else (k-sum(x))//5)