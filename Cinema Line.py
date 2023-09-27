from collections import defaultdict
d=defaultdict(lambda:0)

n=int(input())
x=list(map(int,input().split()))

flag=True
for i in x:
    if i == 50:
        if d[25]<=0:
            flag=False
            # print(1)
            break
        else:
            d[25]-=1
    elif i==100:
        # if d[50]<=0 or d[25]<=0:
        #     flag=False
        #     break
        if d[50] >= 1 and d[25] >= 1:
            d[50] -= 1
            d[25] -= 1
        elif d[25]>=3:
            d[25]-=3
        else:
            flag=False
            break
    d[i]+=1
    # print(dict(d))

print("YES" if flag else "NO")
