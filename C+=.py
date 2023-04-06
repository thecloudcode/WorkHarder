import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    # print(math.ceil(c/(max(a,b))))
    cc=0
    # flag=0
    while(a<=c and b<=c):
        c=a+b
        if a<b:a=c
        else: b=c
        cc+=1
        print(a,b,c,cc)
print(cc)