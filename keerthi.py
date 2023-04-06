# x=input()
# def base10(nn):
#     return(int(nn,10))
# def numberBaseFive(n):
#     # n=str(n,10)
#     print("{0:5}".format(n))
# numberBaseFive(x)
x=int(input())
def numberBaseFive(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(int(n % b)))
        n //= b
    return digits[::-1]
print(''.join(numberBaseFive(x,5)))