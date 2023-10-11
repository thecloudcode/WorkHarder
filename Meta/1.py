n = int(input())
s = " " + input()
tot = [0] * (n + 1)
one = 0
q = int(input())

for _ in range(q):
    i = int(input())
    if i == 1:
        one += 1
        continue
    for j in range(i, n + 1, i):
        tot[j] += 1

ans = 0
for i in range(1, n + 1):
    tot[i] += one

for i in range(1, n + 1):
    tot[i] %= 2
    if tot[i]:
        s = s[:i] + chr(ord(s[i]) ^ 1) + s[i+1:]
    tot[i] = int(s[i])

for i in range(1, n + 1):
    if s[i] == '1':
        ans += 1
        for j in range(i, n + 1, i):
            s = s[:j] + chr(ord(s[j]) ^ 1) + s[j+1:]

print(ans)
