n=int(input())
x=sorted(list(map(int,input().split())))

ind=0
bind=n-1

a=0
bind=0


ind=n//2
a=sum(x[:ind:])
b=sum(x[ind::])

print((a**2)+(b**2))


