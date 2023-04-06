
for _ in range(int(input())):
    m, n, p=map(int,input().split())
    john = 0
    x = []
    for i in range(m):
        a = list(map(int,input().split()))
        x.append(a)
    xx=[]
    for j in range(n):
        for i in x:
            xx.append(i[j])
        john+= max(xx)-xx[p-1]
        xx=[]
    print("Case #"+str(_+1)+":", john)


    # for i in range(m):
    #     a,b,c=map(int,input().split())
    #     # if a+b+c>maxx:
    #     #     maxx=a+b+c
    #     # if i+1==p:
    #     #     xx=a+b+c
    #     aa.append(a)
    #     bb.append(b)
    #     cc.append(c)
    # print(max(aa)-aa[p-1]+max(bb)-bb[p-1]+max(cc)-cc[p-1])
    # print(maxx-xx)

