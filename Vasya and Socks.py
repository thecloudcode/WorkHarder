n,m=map(int,input().split())
c=0
while(n>0):
    c+=1
    if c%m==0 and c!=0:
        n+=1
    n-=1
print(c)