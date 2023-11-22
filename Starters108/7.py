def solve():
    n = int(input())
    if n <= 4:
        print(0, n)
        return
    print(1, n - 1)



for _ in range(int(input())):
    solve()

