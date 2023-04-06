for _ in range(int(input())):
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    a=x[0]
    b=x[1]
    c=y[0]
    d=y[1]
    #13 51 75 37
    #57 73 31 15
    if (a<b and a<c and d>b and d>c) or (b<a and b<d and c>a and c>d) or (a>b and a>c and d<b and d<c) or (b>a and b>d and c<a and c<d):
        print("YES")
    else:
        print("NO")
    # x=a+b
    # x.sort()
    # s=""
    # for i in x:
    #     s+=str(i)
    # s=s+s+s
    # xx=""
    # xxx=""
    # for i in [a[0],a[1],b[0],b[1]]:
    #     xx+=str(i)
    # for i in [a[0],b[0],a[1],b[1]]:
    #     xxx+=str(i)
    # print(s,xx,xxx)
    # # print(s.count(xx),s.count(xxx))
    # #75 47 24
    # #42 25 57
    # if s.count(xx)>0 or s.count(xxx)>0:
    #     print("YES")
    # else:
    #     print("NO")