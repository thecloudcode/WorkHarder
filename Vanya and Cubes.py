import math
n=int(input())
# x=int(math.sqrt(n))
# print((x+1) if (x+1)*(x+2)/2<=n else x if x*(x+1)/2<=n else x-1 if x*(x-1)/2<=n else x-2)
flag=0
summ=0
i=1
while(flag!=-1):
    summ+=i*(i+1)/2
    if summ>n:
        print(i-1)
        flag=-1
        break
    i+=1



