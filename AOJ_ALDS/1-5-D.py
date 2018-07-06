# coding=utf-8


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    reverse = 0
    for i in range(len(a)):
        reverse += sum(1 for x in a[i+1:] if x < a[i])
    print(reverse)
