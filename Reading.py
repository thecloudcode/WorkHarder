n,k=map(int,input().split())
x=list(map(int,input().split()))

xx=x.copy()
xx.sort()
xx=xx[::-1][:k:]
print(xx[k-1])
# print(xx)
ans=[]
for i in range(n):
    if x[i] in xx:
        ans.append(str(i+1))
        xx.remove(x[i])
print(' '.join(ans))
