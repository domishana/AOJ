# coding=utf-8
import array
import math


def sieve_of_eratosthenes(end):
    """
    :type end: int
    :rtype: array.array
    """
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
    N = int(input())
    n = N
    upper_n = int(math.sqrt(n)) + 1
    # print(upper_n)
    prime_list = sieve_of_eratosthenes(upper_n)
    # print(prime_list)
    elementary_number_list = array.array("L")
    counter = 0

    while counter < len(prime_list):
        if n % prime_list[counter] == 0:
            elementary_number_list.append(prime_list[counter])
            n //= prime_list[counter]
        else:
            counter += 1

    if n != 1:
        elementary_number_list.append(n)

    print("{0}: {1}".format(N, ' '.join(map(str, elementary_number_list))))
