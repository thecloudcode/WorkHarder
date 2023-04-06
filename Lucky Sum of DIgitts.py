n=int(input())
four=0
seven=0
while(n>=0):
    if n%7==0:
        seven=n//7
        n=0
        break
    four+=1
    n-=4
if(n==0):
    print('4'*four+'7'*seven)
else:
    print(-1)