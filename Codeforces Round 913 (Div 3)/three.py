import sys
from collections import defaultdict

mod = 10 ** 9 + 7


def mul(x, y):
    x %= mod
    y %= mod
    x += mod
    y += mod
    return (x * y) % mod

def power(x, y):
    x %= mod
    res = 1
    while y:
        if y & 1:
            res = (res * x) % mod
        x = (x * x) % mod
        y //= 2
    return res

def add(x, y):
    x %= mod
    y %= mod
    x += mod
    y += mod
    return (x + y) % mod


for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    mp = defaultdict(int)
    for x in s:
        mp[x] += 1

    maxi = 0
    for x in mp:
        maxi = max(maxi, mp[x])

    if maxi - (n - maxi) <= 0:
        if n % 2 == 1:
            print(1)
        else:
            print(0)
    else:
        print(maxi - (n - maxi))


