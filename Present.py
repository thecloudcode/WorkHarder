n=int(input())
x=list(map(int,input().split()))
xx=[]
for i in range(n):
    xx.insert(str(i+1),x[i])
print(' '.join(xx))