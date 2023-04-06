for _ in range(int(input())):
    n, s=map(str,input().split())
    n=int(n)
    n+=n
    x=input()
    x=list(x+x)
    green=[]
    for i in range(n):
        if x[n-i-1]!='g':
            if len(green)==0 or green[0]==-1:
                green.insert(0,-1)
            else:
                green.insert(0,green[0])
        elif x[n-i-1]=='g':
            green.insert(0,n-i-1)
    # print(green)
    maxwait=-1
    for i in range(n):
        if x[i]==s:
            maxwait=max(maxwait,green[i]-i)
    print(maxwait)