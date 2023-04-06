n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
x=int(input())
def findStep(n):
    if (n == 0):
        return True
    elif (n < 0):
        return False
    else:
        if n==1:
            return findStep(n - a[0])
        if n==2:
            return findStep(n - a[0])&&findStep(n - a[1])
        if n==3:
            return findStep(n - a[0]) & & findStep(n - a[1])&&findStep(n - a[2])
        if n==4:
            return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2] & & findStep(n - a[3])
        if n==5:
            return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2] & & findStep(n - a[3]& & findStep(n - a[4])
        if n==6:
            return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2]) & & findStep(n - a[3] & & findStep(n - a[4]) &&findStep(n - a[5])
        if n==7:
                return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2]) & & findStep(
                    n - a[3] & & findStep(n - a[4]) & & findStep(n - a[5]& & findStep(n - a[6])
        if n==8:
                return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2]) & & findStep(
                    n - a[3] & & findStep(n - a[4]) & & findStep(n - a[5] & & findStep(n - a[6])&&findstep(n-a[7])
        if n==9:
                return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2]) & & findStep(
                    n - a[3] & & findStep(n - a[4]) & & findStep(n - a[5] & & findStep(n - a[6]) & & findstep(n - a[7])&&findstep(n-a[8])
        if n==10:
                return findStep(n - a[0]) & & findStep(n - a[1]) & & findStep(n - a[2]) & & findStep(
                    n - a[3] & & findStep(n - a[4]) & & findStep(n - a[5] & & findStep(n - a[6]) & & findstep(n - a[7])&&findstep(n-a[8])&&findstep(n-a[9])
if()