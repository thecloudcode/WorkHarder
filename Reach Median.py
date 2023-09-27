import bisect
from bisect import bisect_right, bisect_left
# print(bisect_right([1,3],2))
# print(bisect_left([1,1,2,3],1))
n,s=map(int,input().split())
x=sorted(list(map(int,input().split())))

middle=x[n//2]
if s==middle:
    print(0)
elif s<middle:
    ind=bisect_right(x,s)
    c=0
    for i in range(ind,(n//2)+1):
        c+=abs(s-x[i])

    print(c)
else:
    ind = bisect_left(x, s)
    c = 0
    for i in range(n // 2, ind):
        c += abs(s - x[i])
    # if len(x)>ind+1:
    #     c+=abs(s-x[ind])
    print(c)