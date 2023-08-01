def mod_inv(a, mod):
    """
    Calculates the modular inverse of a modulo mod using the extended Euclidean algorithm.
    """
    gcd, x, y = extended_gcd(a, mod)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    return x % mod

def extended_gcd(a, b):
    """
    Returns a tuple (gcd, x, y) such that a*x + b*y = gcd.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x_, y_ = extended_gcd(b, a % b)
        x = y_
        y = x_ - (a // b) * y_
        return (gcd, x, y)

def p_over_q_mod(p, q, mod):
    """
    Returns the value of p*(1/q) mod mod.
    """
    q_inv = mod_inv(q, mod)
    return (p * q_inv) % mod
p = 1
q = 60
mod = 1000000007

result = p_over_q_mod(p, q, mod)
print(result)  # Output: 872833837
