n=int(input())
x=list(map(int,input().split()))
if n==2:
    print(2)
elif n==1:
    print(1)
else:
    i = n - 1
    maxx=2
    while(i>=2):
        j=[i].copy()[0]
        c = 2
        while(j>=2):
            if x[j]==x[j-1]+x[j-2]:
                c+=1
            else:
                break
            j-=1
        maxx=max(c,maxx)
        i=j-1
    print(maxx)
