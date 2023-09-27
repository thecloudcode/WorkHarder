n,d=map(int,input().split())
x=list(map(int,input().split()))

l=len(x)
c=0
if l<3:
    print(0)
else:
    for i in range(l-2):
        for j in range(2+i,l):
            if abs(x[j]-x[i])<=d:
                c+=j-i-1
    print(c)