t=int(input())
cases=[]

for i in range(t):
    l=int(input())
    s=input()
    m=input()
    n=""

    even=0
    for ii in s:
        if even%2==0:
            n+=ii
        else:
            n=ii+n
        even+=1
    if n==m:
        cases.append("YES")
    else:
        cases.append("NO")


for i in range(len(cases)):
    print(f"Case {i+1}: {cases[i]}")