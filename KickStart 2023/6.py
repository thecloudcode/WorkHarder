for _ in range(int(input())):
    x = input().split()
    n = int(input())
    for i in range(int(input())):
        transformed = set("".join(x[ord(s[ii])-65] for ii in range(len(s))) for s in (input() for _ in range(n)))
        print(f"Case #{_+1}: {'NO' if len(transformed)==n else 'YES'}")
