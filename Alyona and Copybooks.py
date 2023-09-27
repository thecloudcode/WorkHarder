n,a,b,c=map(int,input().split())
x=min(a,min(b,c))
# print(n%4)
if n%4==0:
    print(0)
elif n%4==1:
    print(min(3*a,min(a+b,c)))
elif n%4==2:
    print(min(a+a,min(b, c+c)))
else:
    print(min(a,min(b+c, c+c+c)))

