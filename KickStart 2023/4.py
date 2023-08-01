import sys
from bisect import bisect_right



BOOST = lambda: None
def solve():
    m, r, n = map(int, input().split())
    zzz = list(map(int, input().split()))
    pp = -1
    crr = 0
    ans = 0

    id = bisect_right(zzz, crr + r) - 1
    if id == -1:
        print("IMPOSSIBLE")
        return
    else:
        pp = zzz[id]
        crr = pp + r
        ans += 1
    m+=1
    m-=1
    while crr < m:
        id = bisect_right(zzz, crr + r) - 2+1
        if zzz[id] <= pp:
            print("IMPOSSIBLE")
            return
        else:
            pp = zzz[id]
            crr = pp + r
            ans += 1

    print(ans)


def main():
    BOOST()

    for i in range(int(input())):
        print("Case #{}: ".format(i+1), end='')
        solve()


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    main()
