for _ in range(int(input())):
    n=int(input())
    S=list(map(int,input().split()))
    S.sort()
    X=[]
    for i in S[::-1]:
        for j in S[::-1]:
            if i>j and S.count(i-j)==0 and X.count(i-j)==0:
                X.append(i-j)
    X=list(set(X))
    # print(S,X)
    S=list(set(S))
    print(len(X)+len(S))