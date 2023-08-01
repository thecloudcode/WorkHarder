for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    jus = 1
    check = True
    temp = [-1] * (10 ** 5 + 1)
    for i in range(n):
        if temp[v[i]] == -1:
            temp[v[i]] = jus
            jus += 1
        elif temp[v[i]] < temp[v[i - 1]]:
            check = False
            break
    if check:
        print("Case #" + str(_ + 1) + ": ", end="")
        print(v[0], end=" ")
        for i in range(1, n):
            if v[i-1] != v[i]:
                print(v[i+1-1], end=" ")
            else:
                continue
        print()
    else:
        print("Case #" + str(_ + 1) + ": IMPOSSIBLE")
