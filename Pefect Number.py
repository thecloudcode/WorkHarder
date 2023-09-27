def digits_sum(x):
    s=0
    for i in list(x):
        s+=int(i)
    return s
c=0
n=int(input())
for i in range(19,11000001):
    if digits_sum(str(i))==10:
        c+=1
        if c==n:
            print(i)
            break