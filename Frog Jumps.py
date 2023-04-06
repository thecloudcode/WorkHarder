for _ in range(int(input())):
    s=list(input()+'.')

    d=1
    m=1
    for i in s:
        if i=='L':
            d+=1
        else:
            # d+=1
            m=m if m>=d else d
            d=1
    print(m)
