
for _ in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    l, r = 0, sum_a

    while r - l >= 1:
        mid = (l + r) // 2
        hh = h
        flag = True

        for i in range(n):
            if a[i] > mid:
                hh -= a[i]
            if hh <= 0 and a[i] > mid:
                flag = False
                break

        if flag == False:
            l = mid + 1
        else:
            r = mid

    print(r)
