# coding=utf-8


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
S = set(S)
T = set(T)

satisfied_set = S & T

C = len(satisfied_set)

print(C)
