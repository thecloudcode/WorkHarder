import math
n,k=map(int,input().split())
total_time=240-k
summ=0
i=1

while(1):
    summ+=5*i

    if summ>total_time:
        print(i-1)
        break
    if i==n:
        print(i)
        break
    i+=1