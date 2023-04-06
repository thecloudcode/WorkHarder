n,k=map(int,input().split())
x=list(map(str,input().split()))

c=0
for i in x:
    if (i.count('4')+i.count('7'))<=k:
        c+=1
print(c)