from collections import defaultdict
import math

def sum_of_goodness(arr):
    goodness_sum = 0

    for index, num in enumerate(arr):
        contribution = num - index
        goodness_sum = (goodness_sum + contribution) % (10**9 + 7)

    return goodness_sum

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    # a,b=map(int,input().split())
    # s=input()
    # d=defaultdict(lambda:0)
    print(sum_of_goodness(x))