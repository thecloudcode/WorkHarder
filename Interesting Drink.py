from bisect import bisect_right
n=int(input())
x=sorted(list(map(int,input().split())))
# q=int(input())
for i in range(int(input())):
    z=int(input())
    print(bisect_right(x,z))