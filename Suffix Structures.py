

from collections import defaultdict
d=defaultdict(lambda : 0)
dd=defaultdict(lambda : 0)

a=input()
b=input()

def CommonSubsequencesCount(s1, s2):
    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n

first = False
second = False
needfirst = False

# print(CommonSubsequencesCount(b,a))

if CommonSubsequencesCount(b,a):
    first=True
else:
    second=True
    for i in a:
        d[i] += 1
    for i in b:
        dd[i] += 1

    for i in b:
        # if d[i] > dd[i]:
            # needfirst=True
        if d[i] < dd[i]:
            second = False
            break

    if second and len(a)!=len(b):
        first = True
print("both" if (first and second) else "automaton" if first else "array" if second else "need tree")

