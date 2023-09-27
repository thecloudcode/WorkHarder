for _ in range(int(input())):
    x=list(map(int,input().split()))
    maxx=0
    maxc=0
    for i in x:
        if i>maxx:
            maxx=i
            maxc=1
        elif i==maxx:
            maxc+=1
    if maxc>1:
        for i in x:
            print(maxx-i+1,end=" ")
    else:
        for i in x:
            if i==maxx:
                print(0,end=" ")
            else:
                print(maxx-i+1,end=" ")
    print()



