# num=int(input())
# if num%2==0:
#     print("You entered an even number")
# else:
#     print("You entered an odd number")

# ---------------------------------------------

# a=int(input())
# b=int(input())
# print("Addition: ",a+b)
# print("Subtraction: ",a-b)
# print("Multiplication: ",a*b)
# print("Division: ",a/b)

# ---------------------------------------------

# str=input()
# count=0
# for i in str:
#     if i.lower() in "aeiou":
#         count+=1
# print("Number of vowels: ",count)

# ---------------------------------------------

# def factorial(n):
#     fac=1
#     for i in range(2,n+1):
#         fac*=i
#     print(fac)
# factorial(int(input("Enter number: ")))

# ---------------------------------------------

# for i in range(1,51):
#     if i%2==0:
#         continue
#     else:
#         print(i,end=", ")
# print()

# ---------------------------------------------

# n=int(input())
# a=0
# b=1
# if n==1:
#     print("0")
# elif n==2:
#     print("0, 1")
# else:
#     print("0, 1",end=", ")
#     while(n>2):
#         c=a+b
#         print(c,end=", ")
#         a=b
#         b=c
#         n-=1
#     print()

#------------------------------------------------

# treasure=["ruby","sapphire","Diamond","green stone"]
#
# search_item=input("Enter the search Item: ")
# for item in treasure:
#     if(item==search_item):
#         print("Found!")
#         break
# else:
#     print("Not Found!")

#------------------------------------------------
# i=7
# while(i>0):
#     print("while works!",end=", ")
#     i-=1
# else:
#     print("ends")

# -------------------------------------------------

# print("Python program to verify if a given number is prime")
#
# n=int(input("Enter the number : "))
#
# for div in range(2,n):
#     if n%div==0:
#         print("not prime, divisible by", div)
#         break
# else:
#     print("Prime")

#--------------------------------------------------------

# def bmi(a,b):
#     return a/(b**2)
# h=[1.87,1.87,1.82,1.91,1.90,1.85]
# w=[81.65,97.52,95.25,92.98,86.18,88.45]
#
# for i,j in zip(h,w):
#     print(bmi(i,j))

#---------------------------------------------------------

# list=[]
# while(True):
#     x=input()
#     if x.lower()=='stop':
#         print(list)
#         break
#     else:
#         list.append(int(x))

#---------------------------------------------------------

# print([i for i in range(1,101) if i%2==0])

#---------------------------------------------------------

# original=[]
# for i in range(10):
#     original.append(input())
# final=[]
# for i in original:
#     if len(i)<=5:
#         final.append(i)
# print(final)

#---------------------------------------------------------

# num=int(input("Enter number: "))
# str=input('Enter string: ')
# l=list(input('Enter list: '))
#
# x=(num, str, l)
# print(x)

#---------------------------------------------------------

str=input("Enter string: ")
print((str,str[::-1]))