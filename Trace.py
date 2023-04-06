import math

n=int(input())
x=list(map(int,input().split()))
if len(x)%2==1:
    x.append(0)
x.sort()
x=x[::-1]
s=0
i=0
while(i<len(x)):
    s+=(x[i]**2)-(x[i+1]**2)
    i+=2
print('%.10f'%(math.pi*s))
