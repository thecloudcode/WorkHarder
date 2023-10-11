from bisect import bisect_right
# print(bisect_right([1],1))
def cal(a,b,c):
    return abs(b-a)+abs(b-c)
for _ in range(int(input())):
    n=int(input())
    x=sorted(list(set(list(map(int,input().split())))))

    a=bisect_right(x,x[0])-1
    if a>=len(x)-1:
        b=x[-1]
    else:
        b=x[a+1]
    print(x[a],b,x[-1])
    case1=cal(x[a],b,x[-1])
    case2=cal(x[-1],x[a],b)
    case3=cal(x[a],x[-1],b)
    case4=cal(x[-1],b,x[a])
    print(case1,case2,case3,case4)
    print(max(case1,max(case2,max(case3,case4))))
