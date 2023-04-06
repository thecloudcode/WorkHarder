from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    d= defaultdict(lambda: 0)
    dd= defaultdict(lambda: 0)
    x=[1]
    d[s[0]]+=1
    for i in range(1,n):
        # x.append(len(set(s[i::]))+len(set(s[:i:])))
        if s[i] not in list(d.keys()):
            x.append(1+x[i-1])
        else:
            x.append(x[i-1])
        d[s[i]]+=1

    yy={}
    for i in range(n):
        yy[i]=0
    yy[n-1]=1
    # y=[1]
    dd[s[n-1]]+=1
    i=n-2
    while(i>=0):
        if s[i] not in list(dd.keys()):
            yy[i]=1+yy[i+1]
        else:
            yy[i]=yy[i+1]
        dd[s[i]]+=1
        i-=1
    # for i in range(0,n-1):
    #     if s[i] not in list(dd.keys()):
    #         y.append(1+y[i-1])
    #     else:
    #         y.append(y[i-1])
    #     dd[s[i]]+=1
    # y=y[::-1]
    ans=0
    for i in range(n) :
        ans=max(ans,x[i]+yy[i])
    if ans>n:
        ans=n
    print(ans)

    # print(max(x))


    # # f=-1
    # # for i in s:
    # #     if i not in x:
    # #         x.append(i)
    # #     elif i not in y:
    # #         y.append(i)
    # # print(len(x)+len(y))
    # f=0
    # for i in range(n-1):
    #     if s[i]==s[i+1]:
    #         f=i
    #         break
    # print(s[:f+1:],s[f+1::])
    # print(len(set(s)) if f==-1 else len(set(s[:f+1:]))+len(set(s[f+1::])))