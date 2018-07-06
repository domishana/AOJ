# coding=utf-8
import math


while True:
    n = int(input())
    if n == 0:
        break
    S = list(map(int, input().split()))
    average = sum(S)/len(S)
    square_sum = sum(math.pow((score-average), 2) for score in S)
    variance = square_sum/len(S)
    print(math.sqrt(variance))
