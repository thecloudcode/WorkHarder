
# print('@'.join(list(set(list(input()))))+'@')
s=list(map(str,input().split(" ")))
x=int(input())
for i in s:
    if len(i)>x:
        print(i)