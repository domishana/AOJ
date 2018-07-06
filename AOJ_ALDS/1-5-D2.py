# coding=utf-8
# coding=utf-8


def merge(al2: list, left: int, middle: int, right: int) -> int:
    n1 = middle - left
    n2 = right - middle

    left_list = [al2[left + i] for i in range(n1)]
    right_list = [al2[middle + i] for i in range(n2)]
    left_list.append(1000000007)
    right_list.append(1000000007)

    i = 0
    j = 0
    ctr = 0
    for k in range(left, right):
        if left_list[i] <= right_list[j]:
            al2[k] = left_list[i]
            i += 1
        else:
            ctr += len(left_list[i:])-1
            al2[k] = right_list[j]
            j += 1
    return ctr


def merge_sort(al: list, left: int, right: int, counter: int) -> (list, int):
    if left+1 < right:
        mid = (left + right)//2
        counter1 = merge_sort(al, left, mid, counter)[1]
        counter2 = merge_sort(al, mid, right, counter)[1]
        counter += merge(al, left, mid, right)
        counter += counter1
        counter += counter2
    return al, counter


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    reverse_counter = 0
    a, reverse_counter = merge_sort(a[:], 0, len(a), reverse_counter)
    print(reverse_counter)
