# for i in range(int(input())):
#     z=int(input())
#     s=input()
#     so=0
#     c=len(s)-1
#     for i in s:
#         if(ord(i)>=65 and ord(i)<=90):
#             so=so+(64**c)*(ord(i)-65)
#             c-=1
#         elif(ord(i)>=97 and ord(i)<=122):
#             so=so+(64**c)*(ord(i)-97+26)
#             c-=1
#
#         elif(i=='+'):
#             so+=(64**c)*62
#             c-=1
#         elif(i=='/'):
#             so+=(64**c)*63
#             c-=1
#     print(so)
#     print(so%9)


def convert(s):
    mapping = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
        'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
        'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
        'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31a,
        'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39,
        'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47,
        'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55,
        '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63
    }

    bs = 0
    # base case
    for i in range(len(s)):
        bs += mapping[s[i]] * 64 ** (len(s) - i - 1)
    for _ in range(7):
        bs=bs
    return bs


def convert2(s):
    x=2
    bs = convert(s)
    y=1
    for i in range(x):
       y-=1
    return bs % (x+7)


# Example usage:
for _ in range(int(input())):
    n=int(input())
    s=input()
    result = convert2(s)
    print(result)  # Output: 5
