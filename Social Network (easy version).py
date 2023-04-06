a,b=map(int,input().split())
x=list(map(str,input().split()))
s=[]

for i in x:
    if i not in s:
        s.append(i)
xx=b if b<len(s) else len(s)
print(xx)
print(' '.join(s[:xx:][::-1])+" ")
