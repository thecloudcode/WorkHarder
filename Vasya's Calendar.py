d=int(input())
n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(n-1):
    c+=d-(x[i])
print(c)