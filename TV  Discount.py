for _ in range(int(input())):
    x=list(map(int,input().split()))
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    print("First" if a-c<b-d else "Second" if b-d<a-c else "Any")