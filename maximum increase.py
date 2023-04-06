n=int(input())
a=list(map(int,input().split()))

x=[]
c=1
if n==1:
    print(1)
else:
    for i in range(n-1):
        if a[i]<a[i+1]:
            c+=1
        elif a[i]>=a[i+1]:
            x.append(c)
            if i!=n-2:
                c=1
        if i==n-2:
            x.append(c)
            c=1
    print(max(x))

