
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=[0]
    y=[0]
    p=0
    for i in range(n):
        x.append(-1)
        y.append(-1)
#     d={}
#     dd={}
#     xx=[i for i in range(1,n+1)]
#     for i in x:
#         d[i]=xx.index(i)
#         dd[i]=[k for k in range(1,i+1)]
#     for i in x:
#         if x.count(i)<len(dd[i]):
#             print("NO")
#             break
#         else:
#             print("YES")
#             s=""
#             for j,i in dd.items():
#                 if len(i)==1:
#                     s+=str(i[-1])+" "
#                 elif len(i)>0:
#                     s+=str(i[-1])+" "
#                     d[j]=i[:-1:]
#             print(s[:-1:])
