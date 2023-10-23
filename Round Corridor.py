from math import gcd

def main():
    n, m, t = map(int, input().split())
    a = [0, 0]
    g = gcd(n, m)
    a[0] = n // g
    a[1] = m // g

    for _ in range(t):
        x, y, u, v = map(int, input().split())
        c1 = (y // a[x-1]) + int(y % a[x-1] != 0)
        c2 = (v // a[u-1]) + int(v % a[u-1] != 0)
        if c1 == c2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
