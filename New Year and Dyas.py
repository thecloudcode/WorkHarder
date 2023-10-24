s=input()
space=s.index(' ')
n=int(s[:space:])
if s[-1]=='k':
    if n==5:
        print((365//7)+1)
    if n==6:
        print((364 // 7) + 1)
    if n==7:
        print((363 // 7) + 1)
    if n==1:
        print((362 // 7) + 1)
    if n==2:
        print((361 // 7) + 1)
    if n==3:
        print((360 // 7) + 1)
    if n==4:
        print((359 // 7) + 1)
else:
    if n<=29:
        print(12)
    elif n==30:
        print(11)
    else:
        print(7)