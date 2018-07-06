# coding=utf-8
import math


N = int(input())
for i in range(N):
    length_list = list(map(int, input().split()))
    length_list.sort()
    if math.pow(length_list[0], 2) + math.pow(length_list[1], 2) == math.pow(length_list[2], 2):
        print('YES')
    else:
        print('NO')
