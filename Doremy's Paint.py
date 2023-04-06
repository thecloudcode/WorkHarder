for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ind=0
    ind2=ind+1
    d={}
    for i in a[:-1:]:
        for j in a[ind::]:
            print(a[ind],a[ind2])
            d[ind2+1-(ind+1)-len(set(a[ind:ind2+1:]))]=[ind,ind2]
            ind2+=1
            if ind2==len(a):
                ind2=ind
        ind+=1
    x=max(list(d.keys()))
    s=""
    for i in d[x]:
        s+=str(i)+" "
    print(s[:-1:])
    print(d)