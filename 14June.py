# def prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
#
# even={i for i in range(1,11) if i%2 ==0}
# prime={i for i in range(1,11) if prime(i)}
#
# print("Union : ", even | prime)
# print("Intersection : ", even & prime)
# print("Difference : ", even - prime)

#-----------------------------------------------

# s = input("Enter sentence : ")
# words=set(map(str,s.split(' ')))
#
# print("Set of all words: ", words)
# print("Number of unique words: ", len(words))

#-----------------------------------------------

# d={}
# while(True):
#     x=list(map(str,input().split(', ')))
#     if x[0].lower()=='stop':
#         break
#     d[x[0]]=x[1]
# print(d)

#-----------------------------------------------

# from collections import Counter
# print(dict(Counter(input("Enter string: "))))

#-----------------------------------------------

# def discounted(p,d=10):
#     return (1-d/100)*p
# print(discounted(int(input("Enter price: ")),int(input("Enter discount: "))))

#-----------------------------------------------

# def concatenation(a,b,c='-'):
#     return a+c+b
# print(concatenation(input("Enter string1: "),input("Enter string2: "),input("Enter seperator: ")))
# print(concatenation('badal','singh'))

#-----------------------------------------------

# def student_details(n='Unknown',a='Unknown',g='N/A'):
#     return "Name: "+n+", Age: "+a+", Grade: "+g
# print(student_details(input("Enter Name: "),input("Enter Age: "),input("Enter Grade: ")))
# print(student_details())

#-----------------------------------------------

# def get_file_info(filename="Untitled", extension="txt"):
#     return(f"File: {filename}, Extension: {extension}")
# print(get_file_info(input("Enter filename: "),input("Enter extension: ")))

#----------------------------------------------

# product = lambda x, y: x * y
# print(product(3,3))

#-----------------------------------------------

# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else: return(fib(n-1)+fib(n-2))
#
# print(fib(int(input("Enter nth number: "))))

#-----------------------------------------------

# def keyword_arg(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# d={"A":1,"B":2}
# print(keyword_arg(**d))

#------------------------------------------------

# even_check = lambda x: x%2==0
# print(even_check(4))

#------------------------------------------------

# rev = lambda s:s[::-1]
# print(rev('Manchester is Blue'))

#------------------------------------------------
#
# def avg(*avg):
#     return sum(avg)/len(avg)
# print(avg(*[1,1,1,1]))

#------------------------------------------------

# def key_args(**d):
#     print(sorted(d.keys()))
# key_args(**{"Z":1, "A":2})