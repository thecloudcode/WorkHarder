import math

n=int(input())
p=list(map(int,input().split()))
x=list(map(int,input().split()))
xx=[0,0,0,0,0]


letsgo=0
for i in p:
    letsgo+=i
    while(letsgo>=min(x)):
        dif = max(x) + 1
        xxx=-1
        for j in range(len(x)):
            if(letsgo - x[j]<0):
                continue
            elif(letsgo-x[j]<dif):
                dif=letsgo-x[j]
                xxx=j
        # print(letsgo, xx)
        xx[xxx]+=math.floor(letsgo/x[xxx])
        letsgo%=x[xxx]
        # print(letsgo, xx)
for i in xx:
    print(i,end=" ")
print("\n"+str(letsgo))
