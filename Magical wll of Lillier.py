for _ in range(int(input())):
    L=int(input())
    vhl=1
    whl=L
    x=L
    # xx=
    for i in range(2,L+1):
        # print((L%i*2)+vhl+4)
        if ((((L//i)-1)*2)+i+4+(L-(L//i)*i))<x:
            x=(((L//i)-1)*2)+i+4+(L-(L//i)*i)
            # print(x,i)
    print("Case #"+str(_+1)+":",min(L,x))


























