for _ in range(int(input())):
    r,rr=map(int,input().split())
    n=int(input())
    a=0
    b=0
    # mina=(r+rr)*2
    # minb=(r+rr)*2
    aa=[(r+rr)*2]
    bb=[(r+rr)*2]
    for i in range(n):
        x,y=map(int,input().split())
        if (abs(x)**2+abs(y)**2)**(0.5)<=r+rr:
            aa.append((abs(x)**2+abs(y)**2)**(0.5))
            # print(x,y)
            # a+=1
    for i in range(int(input())):
        x,y=map(int,input().split())
        if (abs(x)**2+abs(y)**2)**(0.5)<=r+rr:
            bb.append((abs(x)**2+abs(y)**2)**(0.5))
            # print(x,y)
            # b+=1
    if min(aa)<min(bb):
        xxx=[i for i in aa if i<min(bb)]
        a=len(xxx)
    elif min(bb)<min(aa):
        xxx=[i for i in bb if i<min(aa)]
        b=len(xxx)
    print("Case #"+str(_+1)+": "+str(a)+" "+str(b))
