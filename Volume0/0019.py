# coding=utf-8


if __name__ == '__main__':
    factorial = 1
    n = int(input())
    for i in range(1, n+1):
        factorial *= i
    print(factorial)
