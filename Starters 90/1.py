from collections import  defaultdict
import math

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    # a,b=map(int,input().split())
    # s=input()
    # d=defaultdict(lambda:0)
    c=0
    for i in range(n-1):
        if x[i]!=x[i+1]:
            c+=1
    # print(c)

    if x[0]==0:
        ans=['1']
        i = 1
        while (c > 1):
            ans.append(str('0'))
            ans.append(str('1'))
            i += 2
            c -= 2
    else:
        ans=['0']
        i = 1
        while (c > 1):
            ans.append(str('1'))
            ans.append(str('0'))
            i += 2
            c -= 2

    if c==1:
        if ans[-1]=='0':
            ans.append('1')
        else:
            ans.append('0')
        c-=1

    l=n-len(ans)
    if ans[-1]=='0':
        z='0'
    else:
        z='1'
    while(l>0):
        ans.append(z)
        i+=1
        l-=1
    print(' '.join(ans))