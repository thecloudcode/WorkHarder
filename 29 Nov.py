def pp(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = 1
    x = int(input())
    p = 0
    c = 0
    v = 0
    while p < x:
        c += 1
        if pp(x - v)==False:
            v += n
            p += n
            n *= 2
        else:
            p = p + x - v
            break

    print(c if p==x else -1)
