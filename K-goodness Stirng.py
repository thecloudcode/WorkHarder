for T in range(int(input())):
    N,K=map(int,input().split())
    S=input().upper()
    print("Case #"+str(T+1)+":",end=" ")
    c=0
    # print(int(N/2)+1)
    for i in range(0,int(N/2)):
        if(S[i]!=S[(N)-i-1]):
            c+=1
        # print(s[i],s[N-i-1])
    if c>=K:
        print(0)
    else:
        print(abs(K-c))