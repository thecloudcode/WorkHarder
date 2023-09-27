s=input()
n=int(input())

def shift_string(string, k):
    if not string:
        return string
    k %= len(string)
    shifted_string = string[-k:] + string[:-k]
    return shifted_string

for i in range(n):
    l,r,k=map(int,input().split())
    s=s[:l-1:]+shift_string(s[l-1:r:],k)+s[r::]
print(s)