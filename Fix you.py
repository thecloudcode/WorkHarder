for _ in range(int(input())):
    n,m=map(int,input().split())
    x=[]
    c=0
    for i in range(n):
        x.append(list(input()))
        if x[i][-1]=='R':
            c+=1
    c+=x[-1].count('D')
    print(c)