def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False

    # If last characters of two
    # strings are matching
    if string1[m - 1] == string2[n - 1]:
        return isSubSequence(string1, string2, m - 1, n - 1)

    # If last characters are not matching
    return isSubSequence(string1, string2, m, n - 1)

for _ in range(int(input())):
    s=input()
    n=int(input())
    a=input()
    b=input()

    ind=0
    
