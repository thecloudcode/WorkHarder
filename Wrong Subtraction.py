n,k=map(int,input().split())
for i in range(k):
    if str(n)[-1]=='0':
        n/=10
        n=int(n)
    else:
        n-=1
print(n)