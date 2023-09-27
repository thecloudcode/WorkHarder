from collections import defaultdict

import numpy as np

# d = defaultdict(lambda: 0)

d[0] = 1
d[1] = 2
d[2] = 1
last = 2

def appendreverse(l):
    global last  # Move the global statement here
    for i in range(1, l + 1):
        d[l + i] = d[l - i]
        last += 1

n, k = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(d[k + 1])
for i in range(3, n + 1):
    last += 1
    d[last] = i
    appendreverse(last)
# print(list(dict(d).values()))
print(d[k-1])