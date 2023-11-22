import math
for _ in range(int(input())):
    cn = -1
    n = int(input())
    l = list(map(int, input().split()))
    xx = {}
    b=[]
    for i in range(n+1):
        b.append(-1)
    final = float('inf')

    for i in range(n):
        if l[i] in xx :
            pass
        else:
            xx[l[i]] = [-1]

    for i in range(n):
        xx[l[i]].append(i)
        if len(xx[l[i]]) != 2:
            diff = math.ceil((i - xx[l[i]][-2] - 1) / 2.0)
        else:
            diff = i - 1 - xx[l[i]][-2]


        if diff > b[l[i]]:
            b[l[i]] = diff

    for i in range(n + 1):
        if b[i] != -1:
            if b[i] < n - xx[i][-1] - 1:
                b[i] = n - xx[i][-1] - 1

    for i in range(n + 1):
        if b[i] != -1:
            if b[i] < final:
                cn = i
                final = b[i]

    print(cn, final)
