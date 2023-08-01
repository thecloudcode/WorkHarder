import math
from collections import defaultdict
def mod_inv(a, mod):
    gcd, x, y = extended_gcd(a, mod)
    return x % mod

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x_, y_ = extended_gcd(b, a % b)
        x = y_
        y = x_ - (a // b) * y_
        return (gcd, x, y)

def p_over_q_mod(p, q, mod):
    q_inv = mod_inv(q, mod)
    return (p * q_inv) % mod

d = defaultdict(lambda:0)

def f(n):
    q=1
    for i in range(1, n + 1):
        q*=i
    return q

n=int(input())
for _ in range(n):
    # a, b = map(int, input().split())
    # n = int(input())
    # a = int(input())


    x = list(map(int,input().split()))
    d[x[0]]+=1

q=f(n)
p=1
# print(d)
for i in list(d.values()):
    p*=f(i)
result = p_over_q_mod(p, q, 1000000007)
# print(p,q)
print(result)
