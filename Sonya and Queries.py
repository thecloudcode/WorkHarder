from collections import defaultdict
# d=defaultdict(lambda:-1)
d=[]
dd=defaultdict(lambda:0)

def check(x,s):
    x=str(x)
    lx=len(x)
    ls=len(s)
    m=min(lx,ls)
    mm=max(lx,ls)
    for i in range(1,m+1):
        if int(x[-i])%2!=int(s[-i])%2:
            # print(x[-i],s[-i],-i)
            return False
    if mm>m:
        for i in range(mm-m):
            if lx<ls:
                if s[i]!='0':
                    # print(s[i], i,7)
                    return False
            if lx>ls:
                if int(x[i])%2!=0:
                    # print(x[i], i,77)
                    return False

    return True

for _ in range(int(input())):
    s=input()
    # print(dict(d))
    if s[0]=='+':
        x=s[2::]
        if dd[x]==0:
            d.append(x)
        dd[x]+=1
    elif s[0]=='-':
        x=s[2::]
        dd[x]-=1
    else:
        # print(dict(d))
        c=0
        for i in d:
            # print(d)
            if dd[i]<=0:
                continue
            if check(i,s[2::]):
                # print("checking",i,s)
                c+=1*dd[i]
        print(c)