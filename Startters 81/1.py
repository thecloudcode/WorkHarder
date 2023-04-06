import math
#
for _ in range(int(input())):
    a, b = map(int, input().split())

    print("YES" if (a*b<=500 and a<=8) else "NO")
#     n = int(input())
#     s = input()
#     x = list(map(int, input().split()))
