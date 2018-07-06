# coding=utf-8

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        output_list = []
        if i == 0 or i == H-1:
            for j in range(W):
                output_list.append('#')
        else:
            for j in range(W):
                if j == 0 or j == W-1:
                    output_list.append('#')
                else:
                    output_list.append('.')

        print(''.join(output_list))
    print()
