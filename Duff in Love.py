n=int(input())
sq=int(n**0.5)
i=1
maxx=0
ans=True
while(i<=sq):
    if n%i==0:
        l=n//i
        s=i
        if maxx>=l and maxx>=s:
            print(maxx)
            ans=False
            break
        flag1=False
        flag2=False
        j=2
        k=2
        while(j<=l**0.5):
            # print(j<=l**0.5)
            if l%(j**2)==0:
                flag1=True
                break
            else:
                j+=1
        if flag1:
            # print('flag1 not worked')
            while(k<=s**0.5):
                if s%(k**2)==0:
                    flag=True
                    break
                else:
                    k+=1
        if flag1 and flag2:
            continue
        elif flag1== False:
            print(l)
            ans=False
            break
        elif flag2==False:
            maxx=max(maxx,s)
    i+=1
if ans:
    print(maxx)
