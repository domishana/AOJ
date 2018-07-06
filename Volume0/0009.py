# coding=utf-8
import array


def sieve_of_eratosthenes(end: int) -> array:
    # noinspection PyUnusedLocal
    is_prime = array.array('B', (True for i in range(end+1)))
    is_prime[0] = False
    is_prime[1] = False

    primes = array.array("L")
    for i in range(2, end+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, end+1, i):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    prime_table = sieve_of_eratosthenes(1000000)
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        prime_table_under_n = [x for x in prime_table if x <= n]
        print(len(prime_table_under_n))
