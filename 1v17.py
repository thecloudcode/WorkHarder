t = int(input())
for i in range(t):
    x, y, a, b, d = map(int, input().split())
    r1 = x / a
    r2 = y / b
    if r1>=d and r2>=d:
        print("yes")
    else:
        print("no")