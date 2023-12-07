for _ in range(int(input())):
    n = int(input())
    fact = [0] * 11
    fact[0] = 1
    for i in range(1, 11):
        fact[i] = fact[i - 1] * 3

    ans = 1
    while n > 0:
        tmp = 2 + (n % 10)
        n //= 10
        ans *= tmp * (tmp - 1) // 2

    print(ans)

