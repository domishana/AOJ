# coding=utf-8


def square(number: float) -> float:
    return number * number


if __name__ == '__main__':
    while True:
        s = 0
        try:
            d = int(input())
        except EOFError:
            break
        for i in range(600//d):
            s += square(i*d)*d
        print(s)
