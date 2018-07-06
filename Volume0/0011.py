# coding=utf-8


def list_swap(given_list: list, swap_number1: int, swap_number2: int)-> list:
    return_list = given_list[:]
    memo = given_list[swap_number1 - 1]
    return_list[swap_number2 - 1] = memo
    memo = given_list[swap_number2 - 1]
    return_list[swap_number1 - 1] = memo
    return return_list


if __name__ == '__main__':
    w = int(input())
    amida_number = [i for i in range(1, w+1)]
    n = int(input())
    for j in range(n):
        a, b = map(int, input().split(','))
        amida_number = list_swap(amida_number[:], a, b)
    [print(amida_number[k]) for k in range(w)]
