l=[]
for _ in range(int(input())):
    input()
    input()
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    e,f=map(int,input().split())
    if a==c==d==e or a==c==d==f or b==c==d==e or b==c==d==f or a==b==c==e or a==b==c==f or a==b==d==e or a==b==d==f or e==f==a==c or e==f==a==d or e==f==b==c or e==f==b==d:
        l.append("NO")
    else:
        l.append("YES")
for i in l:
    print(i)