# coding=utf-8


def hit_and_blow(answer: list, expect: list) -> tuple:
    hit, blow = 0, 0
    for (i, j) in zip(answer, expect):
        if i == j:
            hit += 1
    answer_set = set(answer)
    expect_set = set(expect)
    blow_set = answer_set & expect_set
    blow = len(blow_set) - hit
    return hit, blow


if __name__ == '__main__':
    while True:
        try:
            answer_number = list(map(int, input().split()))
            expected_number = list(map(int, input().split()))
        except EOFError:
            break
        h, b = hit_and_blow(answer_number, expected_number)
        print(h, b)
