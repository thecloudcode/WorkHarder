a,b=map(int,input().split())
if a==b:
    print("10"*a)
elif b>2*a+2:
    print(-1)
elif a>b+1:
    print(-1)
elif a-b==1:
    print("0"+"10"*b)
else:
    s=""
    while(1):
        if b == a:
            if s[-1]=='0':
                s+="10"*a
                break
            else:
                s+="01"*a
                break
        if b-a>=1 and b>1:
            s+="11"
            b-=2
            if a>=1:
                s+="0"
                a-=1
        # if a==1 and b==1:

        if a==1 and b==0:
            s="0"+s
            break
        if a==0 and b==1:
            if s[-1]=='0':
                s+='1'
                b-=1
                break
        if a==0 and b==0:
            break
        # print(a, b)
    print(s)
