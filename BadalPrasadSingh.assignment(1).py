# 1.	Write a function that takes a list of integers as input and returns the sum of all the even numbers in the list.

def summ(x):
    return sum(i for i in x if i % 2 == 0)

print(summ(list(map(int,input().split()))))

# 2.	Write a function that takes a list of integers as input and returns a list of only the unique numbers in the list.

def unique(lst):
    return list(set(lst))
print(unique(list(map(int,input().split()))))

# 3.	Write a function that takes two lists of integers as input and returns a list containing only the numbers that appear in both lists.

def common(x, y):
    return list(set(x) & set(y))
print(common(list(map(int,input().split())),list(map(int,input().split()))))

# 4.	Write a function that takes a list of strings as input and returns a list of all the strings that have more than 5 characters.

def fivestr(x):
    return [i for i in x if len(i)>5]
print(fivestr(list(map(str,input().split()))))

# 5.	Write a function that takes a list of integers as input and returns the product of all the numbers in the list.

def pro(x):
    p=1
    for i in x:
        p*=i
    return p
print(pro(list(map(int,input().split()))))

# 6.	Write a function that takes a list of integers as input and returns a list of only the odd numbers in the list.

def odd(x):
    return [i for i in x if i%2==1]
print(odd(list(map(int,input().split()))))

# 7.	Write a function that takes a list of strings as input and returns a list of all the strings that contain the letter "a".

def a(x):
    return [i for i in x if 'a' in i]
print(a(list(map(str,input().split()))))

# 8.	Write a function that takes a list of integers as input and returns the largest number in the list.

def maxx(x):
    return max(x)
print(maxx(list(map(int,input().split()))))

# 9.	Write a function that takes a list of strings as input and returns a list of all the strings that start with the letter "a".

def ainstring(x):
    return [i for i in x if i[0]=='a']
print(ainstring(list(map(str,input().split()))))

# 10.	Write a function that takes a list of integers as input and returns a list of only the numbers that are divisible by 3.

def mult3(x):
    return [i for i in x if i%3==0]
print(mult3(list(map(int,input().split()))))