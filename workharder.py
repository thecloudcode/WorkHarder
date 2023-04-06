n,m=map(int,input().split())
a=list(map(int,input().split()))
x=list(map(int,input().split()))
xx=[0]
sum=0
for i in a:
    sum+=i
    xx.append(sum)
ind=1
for i in x:
    if xx[ind]>=i:
        print(ind,i-xx[ind-1])
    else:
        while(xx[ind]<i):
            ind+=1
        print(ind,i-xx[ind-1])


