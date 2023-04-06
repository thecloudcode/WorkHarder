for _ in range(int(input())):
    s=list(input())
    a=""
    b=""
    for i in s:
        a+=i
        b+=i
    print(a+b[::-1])