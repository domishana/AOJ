# coding=utf-8


def calculate_sum_of_digit(number: int) -> int:
    divide_digit = list(str(number))
    divide_digit = map(int, divide_digit)
    sum_of_digit = sum(divide_digit)
    return sum_of_digit


if __name__ == '__main__':
    while True:
        x = int(input())
        if x == 0:
            break
        digit_sum = calculate_sum_of_digit(x)
        print(digit_sum)
