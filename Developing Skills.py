import math

from collections import defaultdict
d=defaultdict(lambda:0)

def sort_by_units_digit(lst):
    return sorted(lst, key=lambda x: str(x)[-1])

n,k = map(int,input().split())
kk=[k].copy()[0]
x = sort_by_units_digit(list(map(int,input().split())))

ans=0
for i in range(n):
    if x[n-i-1]<100 and k-(10-x[n-i-1]%10)>=0 and x[n-i-1]%10!=0:
        k-=(10-x[n-i-1]%10)
        x[n-i-1]=math.ceil(x[n-i-1]/10)*10
        # print(x[n-i-1],k,x[n-i-1]%10)

# print(x)
for i in x:
    if i<100:
        if i+k>=100:
            ans+=10
            k-=100-i
        else:
            i+=k
            ans+=math.ceil(i/10)
            k=0
    else:
        ans+=i//10
print(ans)



