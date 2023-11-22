

for _ in range(int(input())):
    n = int(input())
    s = input()
    xx = [0] * n

    for i in range(n):
        if s[i] != '0':
            xx[i] = -1
        else:
            xx[i] = 1

    flag = False
    for i in range(n - 2, -1, -1):
        xx[i] = xx[i] + xx[i + 1]
        if xx[i] not in [-1, 0, 1]:
            print("NO")
            flag=True
            break


    if flag == False:
        print("YES")
