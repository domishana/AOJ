# coding=utf-8


def making_n(usable_numbers: int, target: int) -> int:
    if usable_numbers == 1:
        if 0 <= target <= 9:
            return 1
        return 0
    count = []
    for i in range(10):
        count.append(making_n(usable_numbers - 1, target - i))
    return sum(count)


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        print(making_n(4, n))
