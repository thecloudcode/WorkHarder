# 11. Write a function that takes two lists of integers as input and returns a list of only the numbers that appear in exactly one of the lists.

def one(x,y):
    z=[i for i in x if i not in y]
    z+=(i for i in y if i not in x)
    return list(set(z))
print(one(list(map(int,input("Enter list 1: ").split())),list(map(int,input("Enter list 2: ").split()))))

# 12.Write a function that takes a list of integers as input and returns a new list with each number doubled.
def double(x):
    return [i*2 for i in x]
print(double(list(map(int,input("Enter list: ").split()))))

# 13.Write a function that takes a list of strings as input and returns a new list with each string reversed.

def rev(x):
    return [i[::-1] for i in x]
print(rev(list(map(str,input("Enter list: ").split()))))

# 14.Write a function that takes a list of integers as input and returns a new list with each number squared.
def sq(x):
    return [i**2 for i in x]
print(sq(list(map(int,input("Enter list: ").split()))))

# 15.Write a function that takes a list of integers as input and returns the smallest number in the list.
def minn(x):
    return min(x)
print(minn(list(map(int,input("Enter list: ").split()))))

# 16. Write a function that takes a list of strings as input and returns the length of the longest string in the list.
def maxx(x):
    return max([len(i) for i in x])
print(maxx(list(map(str,input("Enter list: ").split()))))

# 17.Write a function that takes a list of tuples as input, where each tuple contains a name (string) and an age (integer). The function should return a list of only the names of people who are over 18 years old.
def age(x):
    return [i[0] for i in x if i[1]>18]
print(age([('badal',20),('srinjoy',20)]))

# 18. Write a function that takes a list of integers as input and returns the average of all the numbers in the list.
def avg(x):
    return sum(x)/len(x)
print(avg(list(map(int,input().split()))))

# 19.Write a class called Person with attributes name (string) and age (integer). Write a method called greet that prints a message with the person's name.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print('Hi! my name is',self.name+', I am',self.age,'years old.')

def final(x):
    ans=[]
    for i in x:
        xx=person(i[0],i[1])
        xx.greet()
final([['Badal',20],['srinjoy',20]])

# 20. Write a function that takes a list of tuples as input, where each tuple contains a name (string) and an age (integer). The function should return a list of Person objects.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def objects(x):
    objects = []
    for i,j in x:
        p = person(i, j)
        objects.append(p)
    return objects
x = [("Badal", 20), ("Srinjoy", 20)]
xx = objects(x)
for person in xx:
    print(person.name, person.age)
