n,k=map(int,input().split())
x=list(map(int,input().split()))
x+=x
for i in range(k-1,2*n):
    if x[i]==1:
        print((i%5)+1)
        break