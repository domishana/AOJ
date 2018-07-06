# coding=utf-8


def choose_sum(number_list: list, sum_number: int, number: int) -> int:
    if number == 1:
        if sum_number in number_list:
            return 1
        else:
            return 0
    elif not number_list:
        return 0
    else:
        number_list1 = number_list[:]
        number_list2 = number_list[:]
        number_list1.pop(0)
        used = number_list2.pop(0)
        res = choose_sum(number_list1, sum_number, number) + choose_sum(number_list2, sum_number-used, number-1)
        return res


if __name__ == '__main__':
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            break
        used_numbers = [i for i in range(1, n+1)]
        patterns = choose_sum(used_numbers, x, 3)
        print(patterns)
