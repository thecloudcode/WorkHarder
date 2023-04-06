n,k=map(int,input().split())
x=list(map(int,input().split()))

# print(x[k-1::])

if len(list(set(x[k-1::])))==1:
    ind=0
    for i in x[::-1]:
        if i!=x[k-1]:
            break
        ind+=1
    print(n-ind)
    # print(x[:k-1:][::-1],x[k-1])
    # if x[k-1] in x[:k-1:]:
    #     kk=(k-1)-(x[:k-1:][::-1].index(x[k-1])+1)
    #     print("lol")
    # else:
    #     kk=k-1
    # print(kk)
else:
    print(-1)