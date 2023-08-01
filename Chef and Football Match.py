for _ in range(int(input())):
    aa = -1
    bb = -1
    for __ in range(int(input())):
        n, a, b = map(int, input().split())
        if n == 1:
            aa = a
            bb = b
            print("YES")
        elif a==b:
            aa=bb=a
            print("YES")
        elif aa == -1:
            print("NO")
        else:
            if min(a, b) < max(aa, bb):
                if aa >= bb:
                    if aa > min(a, b):
                        aa = max(a, b)
                        bb = min(a, b)
                elif aa <= bb:
                    if bb > min(a, b):
                        aa = min(a, b)
                        bb = max(a, b)

                print("YES",aa,bb)
            else:
                print("NO")
        print(aa,bb)