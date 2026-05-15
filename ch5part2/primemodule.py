def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def print_primes(n):
    print(get_primes(n))

def get_primes(n):
    return [x for x in range(n) if is_prime(x)]
    