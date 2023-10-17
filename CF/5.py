# Badal Prasad Singh

def xxx(arg):
    if arg != n:
        r = dp[arg]
        if r != -1:
            return r
        else:
            r = min(1 + xxx(arg + 1), 10**18)
            if n > arg + a[arg]:
                r = min(xxx(1 + arg + a[arg]), r)
            dp[arg] = r
        return r
    else:
        return 0

for _ in range(int(input())):

    n = int(input())
    dp = [-1 for i in range(n)]

    a = list(map(int, input().split()))
    print(xxx(0))
