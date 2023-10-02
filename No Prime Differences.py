n,m=map(int,input().split())

xx=[]
i=2
x=[]

def prime(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
while(i<=m*n):
    x.append(i)
    if len(x)==m:
        xx.append(x)
        x=[]
    if i==m*n or i==(m*n)-1:
        i=1
        while(prime(abs(xx[-1][-1]-i))==True or prime(abs(xx[-2][-1]-i))==True):
            i+=2
        i-=2
    i+=2
for i in xx:
    print(i)