import math
from collections import defaultdict
def find(a,b,c):
    if a>=c:
        return -1
    if b>=a:
        return -1
    if c>=b:
        return -1
    i=0
    end=math.pow(2,30)
    while(i<end):
        if b^i<c^i and a^i < b^i :
            return i
        i+=1
    return -1
for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    a,b,c= map(int, input().split())
    # print(find_x(a,b,c))
    res=[]
    c=0

    # for i in range(2^30):
    #     if c ^ i > b ^ i:
    #         if b ^ i > a ^ i:
    #             res.append(i)
    #             c+=1
    ans=find(a,b,c)
    print(-1 if ans==-1 else ans)
    # n = int(input())
    # s = input()
    # x = list(map(int, input().split()))
    # if x[0]<x[1] and x[1]<x[2]:
    #     print((2^30)-1)
    # elif x[0]<x[1] and x[1]>x[2]:
    #     print(x[0])
    # elif x[]