# def fac(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fac(n-1)
#
# print(fac(4))

# def sum_even(x):
#     s=0
#     for i in x:
#         if i%2==0:
#             s+=i
#     return s
# print(sum_even([1,2,3]))

# def palindromestring(s):
#     return s==s[::-1]
# print(palindromestring("MAM"))

# def max_three(a,b,c):
#     return max(a,max(b,c))
# print(max_three(2,3,4))

def sq(a):
    return a*a

def prime(n):
    f=0
    for i in range(2,n-1):
        if n%i==0:
            f+=1
    return True if f==0 else False
print(prime(7))

def rev_list(x):
    return x[::-1]

def common_list(a,b):
    return list(set(a) & set(b))
print(common_list([1,2,3],[2,3,4]))

def av_list(x):
    return sum(x)/len(x)

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def words(s):
    return s.count(' '+1)

def fib(num):
    n1, n2 = 0, 1
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")

def longstr(x):
    max_str=""
    max_len=0
    for i in x:
        if len(i)>max_len:
            max_str=i
    return max_str

def CheckLeap(Year):
    if((Year % 400 == 0) or
        (Year % 100 != 0) and
        (Year % 4 == 0)):
        print("Given Year is a leap Year");
    else:
        print ("Given Year is not a leap Year")

def area_rec(l,b):
    return l*b

def ctof(x):
    fahrenheit_temp = x * 1.8 + 32
    return fahrenheit_temp


def sqRoot(n, l):
    x = n
    count = 0
    while (1):
        count += 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < l):
            break
        x = root
    return root

def vcount(x):
    c=0
    for i in x.lower():
        if i in 'aeiou':
            c+=1
    return c


def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        middle1 = numbers[(n // 2) - 1]
        middle2 = numbers[n // 2]
        median = (middle1 + middle2) / 2
    return median


import random
import string

def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print(password(7))

