from collections import defaultdict

n = int(input())
ans = 0
mp1 = defaultdict(int)
mp2 = defaultdict(int)
mp = defaultdict(int)

for _ in range(n):
    x, y = map(int, input().split())
    ans += mp1[x]
    ans += mp2[y]
    ans -= mp[(x, y)]
    mp1[x] += 1
    mp2[y] += 1
    mp[(x, y)] += 1

print(ans)
