n=int(input())
s=list(input())
x=[]
if len(s)%2==0:
    i=0
    while(i<n):
        x.append(s[i]+s[i+1])
        i+=2
else:
    x.append(s[0]+s[1]+s[2])
    i = 3
    while (i < n):
        x.append(s[i] + s[i + 1])
        i += 2
print('-'.join(x))