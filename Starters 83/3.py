import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    a,p,q = map(int, input().split())
    # n = int(input())
    s = list(input())
    up=[]
    down=[]
    ans=""
    # for i in s:
    #     up.append(122-ord(i))
    #     down.append(ord(i)-97)
    # # print(up,down)
    # for i in range(len(s)):
    #     if up[i]<=p and p>=0:
    #         p-=up[i]
    #         ans+='a'
    #     elif down[i]<=q and q>=0:
    #         q-=down[i]
    #         ans+='a'
    #     elif down[i]>q and q>=0:
    #         ans+=chr(ord(s[i])-q)
    #         q=0
    #     else:
    #         ans+=s[i]
    #     # print(p,q)

    for i in range(a):
        if p>0:
            for j in range(min(25,p)):
                if s[i]!='z':
                    s[i]=chr(ord(s[i])+1)
                else:
                    s[i]='a'
                if s[i]=='b':
                    break
            p-=min(25,p)
        elif q>0:
            for j in range(min(25,q)):
                if s[i]!='a':
                    s[i] = chr(ord(s[i]) - 1)
                else:
                    s[i]='z'
                if s[i]=='y':
                    break
            q-=min(25,q)
        else:
            break
    print(s)
        # x = list(map(int, input().split()))