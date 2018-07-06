# coding=utf-8
def is_made_sum(array: list, target: int) -> bool:
    if target == 0:
        return True
    elif target < 0:
        return False
    elif not array:
        return False
    else:
        choice = array[0]
        result1 = is_made_sum(array[1:], target)
        result2 = is_made_sum(array[1:], target - choice)
        return result1 or result2


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    M = list(map(int, input().split()))

    for i in range(q):
        answer = is_made_sum(A, M[i])
        if answer:
            print('yes')
        else:
            print('no')
