n=int(input())
x=list(map(int,input().split()))

minodd=(10**9)+1
odd=0
even=0
s=0
for i in x:
    if i%2:
        odd+=1
        if i<minodd:
            minodd=i
    else:
        even+=1
    s+=i
if odd%2:
    s-=minodd
print(s)

