n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(1,n+1):
    if i not in x:
        c+=1
print(c)