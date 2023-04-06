import math
T=int(input())
for _ in range(T):
    L,N=map(int,input().split())
    D=C=[]
    for i in range(N):
        x,y=map(str,input().split())
        if y=='C':
            D.append(int(x))
        elif y=='A':
            D.append(-int(x))
        # print(D)
    s=0
    c=0
    ind=0
    for i in D:
        if (s>0 and s+i<0) or (s<0 and s+i>0):
            c+=1
        if s!=0 and s+i==0:
            c+=1
        s+=i
        c+=abs(s)//L
        print(s,c)
        if abs(s)>=5:
            if s<0:
                s-=(math.ceil(s/L))*L
            else:
                s-=(math.floor(s/L))*L
        ind+=1
        print(s,c)
    print("Case #"+str(_+1)+": "+str(c))