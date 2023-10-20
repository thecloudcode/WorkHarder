import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    print(x[0], end=" ")
    flag=False

    for i in range(1, n):
        v = m // x[i] * x[i]
        while x[i] != math.gcd(x[i - 1],v):
            v = v - x[i]
        if i == n-1:
            flag=True
            print(v)
        else:
            print(v, end=" ")
    if(flag==False):
        print()