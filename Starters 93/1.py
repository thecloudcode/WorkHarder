def prime(n):
    if n<=1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

for i in range(1,101):
    print(i,"IS","PRIME" if prime(i) else "NOT PRIME")