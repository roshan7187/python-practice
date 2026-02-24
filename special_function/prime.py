#using map function to find prime numbers in a given range
def is_prime(n):
    if n <= 1:
        return f'{n} is not a prime number'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f'{n} is not a prime number'
    return f'{n} is a prime number'

prime_numbers = map(is_prime, range(1, 20))
#print(list(prime_numbers))

for result in prime_numbers:
    print(result)

