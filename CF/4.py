for _ in range(int(input())):
    n = int(input())
    v, m = list(map(int, input().split())), {}

    for ii in v:
        x = ii
        for i in range(2, int(ii ** 0.5) + 1):
            while x % i == 0:
                m[i] = m.get(i, 0) + 1
                x //= i

        if x != 1:
            m[x] = m.get(x, 0) + 1

    flag = False
    for vv in m.values():
        if vv % n != 0:
            # print("no")
            flag = True
            break

    print("yes" if flag == False else "no")