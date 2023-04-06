for _  in range(int(input())):
    n=int(input())
    # a=list(map(int,input().split()))
    a=input()
    aa=list(map(int,a.split()))
    if("-1 -1" in a):
        print(sum(aa)+4)
    elif("-1" in a):
        print(sum(aa))
    else:
        print(sum(aa)-4)
