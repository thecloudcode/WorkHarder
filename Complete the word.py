import collections
from collections import defaultdict

def getthatout(s):
    d = defaultdict(lambda: 0)
    q=0
    for i in s:
        if i=='?':
            q+=1
        else:
            d[i]+=1
    c=0
    x=[]
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if d[i]==0:
            c+=1
            x.append(i)
    # print(x)
    ss=""
    if q>=c:
        ind=0
        for i in s:
            if i=='?':
                if ind<len(x):
                    ss+=x[ind]
                    ind+=1
                else:
                    ss+="B"
            else:
                ss+=i
        return ss
    else:
        return ""
# print(getthatout("A?????????????????????????"))
s=input()
l=len(s)
ans=""
flag=False
if l<26:
    print(-1)
else:
    i=0
    while(i<l):
        xxx=getthatout(s[i:i+26:])
        if xxx=="":
            ans+=s[i]
            i+=1
        elif flag==False:
            ans+=xxx
            flag=True
            i+=26
        if flag:
            ans+=s[i::]
            break
    # print(s)
    if flag:
        for i in ans:
            if i=='?':
                print("B",end="")
            else:
                print(i,end="")
    else:
        print(-1)