n=int(input())

def find(n,s):
    if s==n:
        return 1
    if s>n:
        return 0
    else:
        return find(n,s+1)+find(n,s+2)+find(n,s+3)+find(n,s+4)+find(n,s+5)+find(n,s+6)

print(find(n,0))