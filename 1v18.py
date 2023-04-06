t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    s=r=0
    for j in a:
        if j=='1':
            s+=1
        else:
            r+=1
    if s > r:
        print("YES")
    else:
        print("NO")