# coding=utf-8

n = int(input())
for i in range(n):
    points_list = list(map(float, input().split()))
    abx = points_list[2] - points_list[0]
    aby = points_list[3] - points_list[1]
    cdx = points_list[6] - points_list[4]
    cdy = points_list[7] - points_list[5]

    if abx == 0 or cdx == 0:
        if abx == 0 and cdx == 0:
            print('YES')
        else:
            print('NO')
    elif aby / abx == cdy / cdx:
        print('YES')
    else:
        print('NO')
