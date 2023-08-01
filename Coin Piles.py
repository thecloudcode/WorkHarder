for _ in range(int(input())):
    a,b=map(int,input().split())
    # 21 11 19 10 17 9 15 8 13 7 11 6 9 5 7 4 5 3 3 2
    x=(2*b-a)/3
    if x==(2*b-a)//3:
        print("YES")
    else:
        print("NO")