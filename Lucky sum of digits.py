n=int(input())
s=""
while(n>0):
    if n%7==0:
        s+=(n//7)*'7'
        n-=(n//7)*7
        break
    else:
        s+="4"
        n-=4
print(s if n==0 else -1)