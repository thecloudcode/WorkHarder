n,d=map(int,input().split())
x=list(map(int,input().split()))

flag=False
for i in range(n-1):
    if((x[i]+x[i+1])%d!=0):
        flag=True
        break

print(2 if flag else 1)