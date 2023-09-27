def find_min_xor(A, B):
    x=0
    d=abs(A^x-B^x)
    for i in range(0,31):
        m=1<<i
        x|=m
        dd=abs(A^x-B^x)
        if dd>=d:
            x^=m
        else:
            d=dd

    print(x)


for _ in range(int(input())):
    # result = find_min_xor(A, B)
    # print(result)
    a,b=map(int,input().split())
    find_min_xor(a,b)