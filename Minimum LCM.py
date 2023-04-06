# import time
# start=time.time()
def llcm(x, y):
   if x > y:
       g = x
   else:
       g = y
   while(True):
       if((g % x == 0) and (g % y == 0)):
           lcm = g
           break
       g += 1
   return lcm

for _ in range(int(input())):
    n = int(input())
    minn = n-1
    a = 1
    b = n-1
    if n%2==0:
        a=n//2
        b=n//2
    else:
        for i in range(1, n):
            print(i,(n-i),llcm(i,n-i))
            if (n-i)%i==0:
                if llcm(i, (n-i)) < minn:
                    minn = llcm(i, (n-i))
                    a = i
                    b = n-i
                    if (i==n-i and n%2==0) or (i==(n//2)+1 and n%2==1):
                        break
    print(a, b)
    # end=time.time()
    # print(end-start)