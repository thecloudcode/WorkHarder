from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))
aa=[]
s=0
for i in a:
    s+=i
    aa.append(s)
# print(aa) lol
n=int(input())
x=list(map(int,input().split()))
for i in x:
    print(bisect_left(aa,i)+1)