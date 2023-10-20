from collections import defaultdict

for _ in range(int(input())):
    d=defaultdict(lambda:0)
    dd=defaultdict(lambda:0)
    n=int(input())

    x=[]
    for i in range(n):
        xx=int(input())
        x.append(xx)
        d[xx]+=1

    xx=[]
    c=0
    for i in x:
        if d[i]>1 and dd[i]==0:
            xx.append(i)
            dd[i]+=1
        elif d[i]>1 and dd[i]>0:
            while(1):
                if i%10==9:
                    i-=9
                else:
                    i+=1
                if d[i]==0:
                    d[i]+=1
                    c+=1
                    xx.append(i)
                    break
        else:
            xx.append(i)
    print(c)
    for i in xx:
        l=len(str(i))
        print("0"*(4-l)+str(i))