from collections import defaultdict
d=defaultdict(lambda:0)

flag=False
a,b,c,e=0,0,0,0
for _ in range(int(input())):
    n=int(input())

    x=list(map(int,input().split()))
    s=sum(x)


    for i in range(n):
        if d[s - x[i]] != 0 and d[s - x[i]][0] != _ + 1 and flag==False:
            flag = True
            a = d[s - x[i]][0]
            b = d[s - x[i]][1]
            c = _ + 1
            e = i + 1
        if flag==False:
            d[s-x[i]]=(_+1,i+1)

if flag:
    print("YES")
    print(a,b)
    print(c,e)
else:
    print("NO")
