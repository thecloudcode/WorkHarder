# Badal Prasad Singh
# Unique XOR

def cal(n, k, s):
    oo, o = [0] * k,[0] * k

    for i in range(n):
        if s[i] != '0':
            o[i%k] += 1
        else:
            oo[i%k] += 1


    final1, final2= 0, 0

    for i in range(k):
        if o[i] % 2 != 1:
            final1 += o[i] // 2
        else:
            final1 += 1 + (o[i] + 1) // 2


    for i in range(k):
        if o[i] != 0:
            final2 += oo[i]
        else:
            final2 = float('inf')
            break

    if final1<final2:
        return final1
    else:
        return final2


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    res = cal(n, k, s)
    print(res)

