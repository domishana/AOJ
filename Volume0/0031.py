# coding=utf-8
import math


def binary_conv(number: int) -> list:
    binary_list = []
    while True:
        binary_list.append(number % 2)
        if number == 1 or number == 0:
            break
        number //= 2
    binary_list.reverse()
    return binary_list


if __name__ == '__main__':
    while True:
        try:
            w = int(input())
        except EOFError:
            break
        weight_list = []
        w_binary = binary_conv(w)
        for i in range(len(w_binary)):
            if w_binary[i] != 0:
                weight_list.append(int(math.pow(2, i)))
        print(' '.join(map(str, weight_list)))
