import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a = map(int, input().split())
    n = int(input())
    # a = int(input())


    s = list(input())
    prev='1'
    c=1
    for i in s[:n-1:]:
        if prev!=i:
            c+=1
            prev='1'
        else:
            prev='0'
    # print(c)
    print(max(c,n-c))

    # x = list(map(int, input().split()))