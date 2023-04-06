n=int(input())
x=list(map(int,input().split()))

ans=[]
for i in range(n):
    c=1
    low=i-1
    high=i+1
    while(low>=0):
        if(x[low]>x[low+1]):
            break
        c+=1
        low-=1
    while(high<=n-1):
        if x[high]>x[high-1]:
            break
        c+=1
        high+=1
    ans.append(c)
print(max(ans))