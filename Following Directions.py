for _ in range(int(input())):
    n=int(input())
    s=list(input())
    x=0
    y=0
    f=False
    for i in s:
        x+=1 if i=='U' else -1 if i=='D' else 0
        y+=1 if i=='R' else -1 if i=='L' else 0
        if(x==1 and y==1):
            f=True
            break

    print("YES" if f else "NO")
