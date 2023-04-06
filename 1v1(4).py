import math
# def prime(num):
#     if num==1:
#         return True
#     if num>2:
#         for i in range(2,num):
#             if num%i==0:
#                 return True
#     return False

def primeFactors(n):
    if (n % 2 == 0):
        d[2] = 0
    while n % 2 == 0:
        d[2] += 1
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            d[i] = 0
        while n % i == 0:
            # print(i)
            d[i] += 1
            n = n / i
    if n > 2:
        d[n] = 1
    return(d)
global d
d={}
print(len(list(primeFactors(int(input())).keys())))