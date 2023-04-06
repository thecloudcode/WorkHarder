n,m=map(int,input().split())
xx=[]
for i in range(m):
    c=int(input())
    x=list(set(list(map(int,input().split()))))
    xx.append(x)
c=0
print(xx)
# lists = [0]
s=[]
for i in range(len(xx) + 1):
    # s=[]
    for j in range(i):
        # s=[]
        for k in xx[j: i]:
            s+=k
            print(s)
            if len(list(set(s)))==n:
                # print(s)
                c+=1
        s=[]
print(c)