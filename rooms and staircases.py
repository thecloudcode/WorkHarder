for _ in range(int(input())):
    n=int(input())
    x=list(input())
    if '1' in x:
        xx=min(x.index('1'),x[::-1].index('1'))
    print((n-xx)*2 if '1' in x else n)