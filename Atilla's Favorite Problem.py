for _ in range(int(input())):
    n=int(input())
    s=sorted(list(input().lower()))
    print(ord(s[-1])-96)