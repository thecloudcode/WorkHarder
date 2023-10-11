for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>=3:
        x=str(b)[-3::]
    else:
        x=str(b)
    x=int(x)
    if x%8==0:
        print(b)
    else:
        xa=str(x+(8-x%8))
        xb=str(x-x%8)
        xa="0"*(3-len(xa))+xa
        xb="0"*(3-len(xb))+xb
        ca=0
        cb=0
        x="0"*(3-len(str(x)))+str(x)
        for i in range(1,4):
            if xa[-i]!=x[-i]:
                ca+=1
            if xb[-i]!=x[-i]:
                cb+=1
        if ca<=cb:
            print(int(str(b)[:-3:]+xa))
        else:
            print(int(str(b)[:-3:]+xb))
