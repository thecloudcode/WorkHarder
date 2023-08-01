for _ in range(int(input())):
    xx=list(map(int,input().split()))
    n=xx[0]
    query=xx[1]
    arr = sorted(list(map(int, input().split())))

    secarr = [0 for i in range(n+1)]
    for _ in range(query):
        x, y = map(int, input().split())
        secarr[y] -= 1
        secarr[x - 1] += 1

    for i in range(1, n + 1):
        secarr[i] += secarr[i - 1]

    xans = []
    for i in range(n):
        xans.append(tuple([secarr[i], i]))
    xans.sort()
    xans=xans[::-1]

    ans = 0
    wans = []
    rp = n - 1
    for i in xans:
        rp -= 1
        wans.append(tuple([i[1], arr[rp+1]]))
        ans += i[0] * arr[rp+1]

    print(ans)
    for i in sorted(wans):
        print(i[1], end=" ")