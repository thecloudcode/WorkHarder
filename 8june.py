import math

# def fac(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fac(n-1)
#
# x=int(input("Enter number : "))
#
# print("Factorial : ", fac(x))
# print("Square roor : ", math.sqrt(x))

# ---------------------------------------

# x=int(input())
# print(math.pow(x,2), math.sin(x),math.tan(x),math.cos(x))

# ---------------------------------------

# x=input()
# print(x[:5:])

# ---------------------------------------

# def twoc(n):
#     bits = n.bit_length()
#     print(bin(n))
#     bitmask = (1 << bits) - 1
#     print(bin(bitmask))
#     twos_comp = (~n & bitmask) + 1
#     print(bin(twos_comp))
#     return twos_comp
#
# n = int(input("Enter a number: "))
# print("Two's complement of", n, "is", twoc(n))

# ----------------------------------------
x=int(input())
print("VOTE AND CONTEST" if x>=25 else "ONLY VOTE" if x>=18 else "NOTHING")
