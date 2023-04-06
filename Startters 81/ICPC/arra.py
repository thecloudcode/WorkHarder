def sub_lists(l):
    lists = []
    for i in range(1,len(l) + 1):
        for j in range(i-1):
            lists.append(l[j: i])
    return lists


# driver code
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))

    summ=0
    xx=sub_lists(x)
    # print(xx)
    for i in xx:
        if len(i)>=2:
            ii=i.copy()
            mm=min(i)
            ii.remove(mm)
            mmm=min(ii)
            summ+=mm^mmm
    print(summ)