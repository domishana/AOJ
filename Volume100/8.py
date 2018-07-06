# coding=utf-8

while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0 and tmp[1] == 0:
        break
    tmp.sort()
    print(' '.join(map(str, tmp)))
