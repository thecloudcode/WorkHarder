from collections import defaultdict
d=defaultdict(lambda : 0)


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    for i in primes:
        d[i]=1

a,b=map(int,input().split())
for i in range(b):
    x=list(map(int,input().split()))


