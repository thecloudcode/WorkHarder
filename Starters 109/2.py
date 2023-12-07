for _ in range(int(input())):
    n , b= int(input()), list(map(int, input().split()))
    xx, x = [], []
    for i in range(n):
        x.append(b[i]) if b[i] & 1 else xx.append(b[i])
    if len(x) % 2 == 1 or len(xx) % 2 == 1:
        print("-1")
        continue
    e, o = len(xx), len(x)

    x.sort(reverse=True)
    b.sort(reverse=True)
    xx.sort(reverse=True)

    a = []
    for i in range(n):
        a.append(0)

    for i in range(o // 2):
        a[i + n // 2] = (x[i] - x[i + o // 2]) // 2

        a[i] = (x[i] + x[i + o // 2]) // 2

    for i in range(e // 2):
        a[len(x) // 2 + i + n // 2] = (xx[i] - xx[i + e // 2]) // 2

        a[len(x) // 2 + i] = (xx[i] + xx[i + e // 2]) // 2

    flag = True
    for i in a:
        print(i, end=' ')

    if flag:
        print()

