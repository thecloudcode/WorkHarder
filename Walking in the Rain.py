n=int(input())
x=list(map(int,input().split()))
xx=[]
xx.append(x[0])
xx.append(x[-1])
for i in range(1,n-1):
    xx.append(max(x[i],x[i+1]))
print(min(xx))