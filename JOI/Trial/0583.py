# coding=utf-8


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    if n1 == n2 or n2 == 0:
        return n1
    n1, n2 = n2, (n1 % n2)
    return gcd(n1, n2)


def make_divisor_list(number):
    divisor_list = []
    if number == 1:
        return [1]

    for i in range(1, number//2 + 1):
        if number % i == 0:
            divisor_list.append(i)
    divisor_list.append(number)
    return divisor_list


if __name__ == '__main__':
    N = int(input())
    number_list = list(map(int, input().split()))
    if N == 2:
        GCD = gcd(number_list[0], number_list[1])
    else:
        GCD = gcd(gcd(number_list[0], number_list[1]), number_list[2])
    [print(element) for element in make_divisor_list(GCD)]
