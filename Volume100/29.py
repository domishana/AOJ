# coding=utf-8

n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
print(' '.join(map(str, numbers)))
