# def perform_math_operations(a,b):
#     print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
#
#     try:
#         while (True):
#             choice=int(input())
#             print(a+b if choice==1 else a-b if choice==2 else a*b if choice==3 else a/b if choice==4 else "Ending")
#             if choice>4 or choice<1:
#                 break
#     except ValueError:
#         print('Enter integers!')
#     except ZeroDivisionError:
#         print('Trying to divide by zero')
#     finally:
#         print('I am done with it')
# perform_math_operations(int(input("Enter first num: ")),int(input("Enter second num: ")))


# class OddNumberError(Exception):
#     pass
# def check_even_num(n):
#     if n%2==0:
#         print("Even number it is!")
#     else:
#         raise OddNumberError("Odd numbers are not allowed!")
# try:
#     check_even_num(int(input("Enter number: ")))
# except OddNumberError as e:
#     print(e)


def inc(x):
    return x+1
def dec(x):
    return x-1
def operate(func,x):
    result=func(x)
    return result
print(operate(inc,int(input())))
print(operate(dec,int(input())))