from collections import defaultdict

d = defaultdict(lambda: 0)

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    a, b = map(int, input().split())

