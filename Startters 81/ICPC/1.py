from collections import defaultdict
import math
#

def find(s,i,n):
    a=find(a,i+1,n)+a
    b=b+find(b,i+1,n)
    if i==n-1:
        return s[i]


for _ in range(int(input())):
    # a, b = map(int, input().split())
    # if a==b:
    #     print("YES")
    # else:
    #     print("NO")
    n = int(input())

    x=input()
    y=input()


#     s = input()
#     x = list(map(int, input().split()))

