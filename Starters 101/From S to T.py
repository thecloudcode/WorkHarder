from collections import defaultdict
for _ in range(int(input())):
    s=input()
    t=input()
    p=input()

    d=defaultdict(lambda:0)
    dd=defaultdict(lambda:0)
    ddd=defaultdict(lambda:0)
    flag=True
    for i in s:
        d[i]+=1
    for i in t:
        dd[i]+=1
    for i in p:
        ddd[i]+=1
    c=0
    for i in set(list(t)):
        if d[i]>dd[i]:
            flag=False
            print("first")
            break
        if d[i]<=dd[i]:
            if d[i]+ddd[i]<dd[i]:
                flag=False
                print("second")
                break
        c+=dd[i]-d[i]
    print(c)
    if c+len(s)==len(t) and flag:
        print("YES")
    else:
        print("NO")
