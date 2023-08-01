from bisect import bisect_right
n=int(input())
x=sorted(list(map(int,input().split())))
# print(x)
maxx=0
for i in range(n):
    # print("lol",bisect_right(x,x[i]+5),i)
        maxx=max(maxx,bisect_right(x,x[i]+5)-i-1)
print(maxx+1)

