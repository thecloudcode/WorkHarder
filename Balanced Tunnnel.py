n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
j=0
while(i<n and j<n):
    if a[i]==b[j]:
        i+=1
        j+=1
    else:
        j+=1
print(n-i-1)