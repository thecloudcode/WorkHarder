import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    n,k = map(int, input().split())
    # n = int(input())
    s=input()
    if s[0]=='0':
        s='1'+s[1::]
        k=k-1
    for i in range(k):
        s+='0'
    print(s)