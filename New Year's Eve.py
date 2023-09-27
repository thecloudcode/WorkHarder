n,k=map(int,input().split())
m=1
while(m<n):
    m=2*m+1
print(m if k!=1 else n)