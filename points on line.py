n,d=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in range(n-2):
    if(abs(x[i+2]-x[i])<=d):
        c+=1
print(c)