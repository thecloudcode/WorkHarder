for _ in range(int(input())):
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    of=0
    h=1
    for i in x:
        if i==h:
            of+=1
            h+=1
    s=a-of
    if s%b==0:
        print(int(s/b))
    else:
        print(int(s/b)+1)

















# for _ in range(int(input())):
#     a,b=map(int,input().split())
#     x=list(map(int,input().split()))
#     z=[i for i in range(1,a+1)]
#     # print(z)
#     xx=[]
#     c=0
#     cc=0
#     flag=False
#     j=0
#     while(j<=4):
#         xxx=x.copy()
#         for i in range(a):
#             if x[i]!=z[i] and len(xx)!=b:
#                 xx.append(x[i])
#                 print(x[i])
#                 xxx.remove(x[i])
#                 c+=1
#                 # print(x,xx)
#             if len(xx)==b:
#                 xx.sort()
#                 xxx.extend(xx)
#                 print(xxx)
#                 xx=[]
#                 x=xxx.copy()
#                 xxx=[]
#                 # print(x)
#                 c=0
#                 cc+=1
#                 # if tuple(x)==tuple(z):
#                 #     flag=True
#                 break
#         j+=1
#     print(cc)