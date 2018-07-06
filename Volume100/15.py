# coding=utf-8

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        output_list = []
        for j in range(W):
            if (i+j) % 2 == 0:
                output_list.append('#')
            else:
                output_list.append('.')

        print(''.join(output_list))
    print()
