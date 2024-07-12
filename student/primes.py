# def write_primes(n, path):
#     '''
#     Write primes under n to a specified file.
#     :param n: int, The number to write primes under.
#     :param path: str, The path to the file to write the primes to.
#     :return: None
#     '''
#     # Delete the contents of the file if it already exists
#     open(path, 'w').close()

#     # Loop over all the possible prime numbers
#     for i in range(2, n + 1):
#         # Check if the number is prime
#         if is_prime(i):
#             #If it is prime, write it to the file
#             with open(path, 'a') as file:
#                 file.write(str(i) + '\n')

# def is_prime(n):
#     '''
#     Check if a number is prime.
#     :param n: int, The number to check.
#     :return: bool, True if the number is prime, False otherwise.
#     '''

#     # 0, 1, and negative numbers are not prime
#     if n < 2:
#         return False
    
#     # Check if the number is divisible by 2 or 3
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
    
#     # Consider all numbers of the form 6k ± 1 up to the square root of n
#     for i in range(5, int(n ** 0.5) + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
    
#     # If no factors have been found, the number is prime
#     return True
from numba import jit

def write_primes(n, path):
    '''
    Write primes under n to a specified file.
    :param n: int, The number to write primes under.
    :param path: str, The path to the file to write the primes to.
    :return: None
    '''
    # Get the list of primes
    primes = sieve_of_eratosthenes(n)
    # Join primes into a single string with newline characters
    primes_str = '\n'.join(map(str, primes)) + '\n'
    # Write all primes to the file at once
    with open(path, 'w') as file:
        file.write(primes_str)

@jit(nopython=True)
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n) if is_prime[i]]
    return primes
