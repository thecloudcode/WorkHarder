# monotonicity


# Find sqrt(x) in log(x) without using ibuilt sqrt() function
def squareroot(n):
    # time complexity : log n
    l = 0
    r = n
    while (l <= r):
        mid = (l + r) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            l = mid + 1
        elif mid * mid > n:
            r = mid - 1
    return mid if mid * mid < n else mid - 1


# print(squareroot(int(input())))

# Binary Search on Answer (Important + Non-Trivial)

# Consider a predicate P defined over some ordered set S (the search
# space). The search space consists of candidate answers to the
# problem. In our case, a predicate is a function which returns
# TRUE or FALSE. We use the predicate to verify if a candidate answer is legal
# or not.

# Example: We have the set of numbers {1,2,3,4,5}. Our predicate
# function could be following:
# Return TRUE if the number is less than 3 and FALSE otherwise
# Now, if we pass 2 to this function, it will return TRUE right?

def find(x):
    l = 0
    r = len(x) - 1
    while (l <= r):
        mid = (l + r) // 2
        while (l <= r):
            if x[mid] == True and x[mid - 1] == False:
                return mid
            elif x[mid] == False:
                l = mid + 1
            elif x[mid] == True:
                r = mid - 1


x = [False, False, True, True, True, True]

# print(find(x))

# FairWorkload Problem

# Given an array of workloads, split it among 'k' workers, such
# that the maximum work that any worker has to do is minimised
# (can't change order of workloads).

# E.g. 10 20 30 40 50 60 70 80 90
# Solution : 10 20 30 40 50 | 60 70 | 80 90
# First Worker : 150, Second Worker : 130, Third Worker : 170

# Is it possible to partition workload in a way that the highest workload
# of any worker is less than 170? Hence, answer is 170

def work(x,k):
    # create an array of sums and find it using binary search
    summ=[]
    xx=0
    for i in x:
        xx+=i
        summ.append(xx)


