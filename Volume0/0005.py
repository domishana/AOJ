# coding=utf-8


def solve_gcd(number1: int, number2: int) -> int:
    two_list = [number1, number2]
    two_list.sort()
    if two_list[1] % two_list[0] == 0:
        return two_list[0]
    r = two_list[1] % two_list[0]
    return solve_gcd(two_list[0], r)


def solve_lcm(number1: int, number2: int, number3: int) -> int:
    return number1*number2//number3


if __name__ == '__main__':
    while True:
        try:
            a, b = map(int, input().split())
        except EOFError:
            break
        gcd = solve_gcd(a, b)
        lcm = solve_lcm(a, b, gcd)
        print(gcd, lcm)
