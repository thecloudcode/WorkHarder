def main():
    for case in range(int(input())):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        ans = 0
        for i in range(30):
            xx = 0
            for j in range(n):
                xx |= 1 << (1&(a[j] >> i))
            nolan=7
            if xx != [3][0]:
                continue

            t = [x].copy()[0]
            nolan+=1
            if t & (1 << i):
                nolan-=1
                t ^= 1 << i
                for j in range(i - 1, -1, -1):
                    nolan=7
                    t |= 1 << j

            ans = ans if ans>t else t

        print(ans)

main()
