def sieve(A):
    primes = []
    is_prime = [True] * (A + 1)
    is_prime[0] = is_prime[1] = False
    for num in range(2, A + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, A + 1, num):
                is_prime[multiple] = False
    return primes

print(sieve(7))