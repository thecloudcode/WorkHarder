t=list(map(int,input().split()))
n=int(input())
lol=['S','M','L','XL','XXL']
for i in range(n):
    x=input()
    ind=lol.index(x)
    low=[ind].copy()[0]
    high=[ind].copy()[0]
    # print(low,high)
    while(low>=0 or high<=len(t)-1):
        if(high<=len(t)-1):
            if t[high]>0:
                print(lol[high])
                t[high] -= 1
                break
        if(low>=0):
            if t[low]>0:
                print(lol[low])
                t[low] -= 1
                break
        low-=1
        high+=1
