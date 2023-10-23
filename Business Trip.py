n=int(input())
x=sorted(list(map(int,input().split())))[::-1]

s=0
i=0
c=0
while(i<12):
    if s>=n:
        break
    s+=x[i]
    c+=1

    i+=1
print(c if s>=n else -1)