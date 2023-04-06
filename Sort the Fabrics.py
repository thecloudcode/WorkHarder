for _ in range(int(input())):
    n=int(input())
    a=[]
    b=[]
    c=[i for i in range(1,n+1)]
    for i in range(n):
        x,y,z=map(str,input().split())
        x+=z
        y+="."+z
        y=float(y)
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    z=0
    for i,j,z in zip(a,b,c):
        if int(i[-1])==z:
            print(i,j,z)
            z+=1
            print(1,z)
        elif z==int(str(j)[str(j).index('.')+1::]):
            print(i, j, z)
            z += 1
            print(2,z)
# from collections import defaultdict
# for _ in range(int(input())):
#     n=int(input())
#     d=defaultdict(int)
#     dd=defaultdict(int)
#     u=[i for i in range(1,n+1)]
#     # y=[]
#     for i in range(n):
#         a,b,c=map(str,input().split())
#         d[a]=int(c)
#         dd[int(b)]=int(c)
#     x=sorted(list(d.keys()))
#     y=sorted(list(dd.keys()))
#     xx=[d[i] for i in x]
#     yy=[dd[i] for i in y]
#     c=0
#     print(xx,yy,u)
#     for i,j,k in zip(xx,yy,u):
#         print(i,j,k)
#         if i==k or j==k:
#             c+=1
#     print(c)
#     # y=sorted(list())
#
