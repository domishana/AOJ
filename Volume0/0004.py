# coding=utf-8

while True:
    try:
        number_list = list(map(float, input().split()))
    except EOFError:
        break
    det = number_list[0]*number_list[4] - number_list[1]*number_list[3]
    inverse_list = [number_list[4] / det, -number_list[1] / det, -number_list[3] / det, number_list[0] / det]

    x = inverse_list[0]*number_list[2] + inverse_list[1]*number_list[5]
    y = inverse_list[2]*number_list[2] + inverse_list[3]*number_list[5]

    print('{0:.3f} {1:.3f}'.format(x, y))
