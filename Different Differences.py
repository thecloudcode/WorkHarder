for _ in range(int(input())):
    a,b=map(int,input().split())
    x=[i for i in range(1,b+1)]
    i=1
    xx=""
    f=0
    while(i<=b):
        xx+=str(i)+" "
        x.remove(i)
        f+=1
        i+=f
    if len(xx)//2<a:
        for i in range(a-len(xx)//2):
            xx+=str((x[-(a-len(xx)//2-i)]))+" "
    print(xx[:-1:])