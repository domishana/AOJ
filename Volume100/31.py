# coding=utf-8


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
C = 0

for i in range(q):
    if T[i] in S:
        C += 1
print(C)
