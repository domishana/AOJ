# coding=utf-8

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        output_list = []
        for j in range(W):
            output_list.append('#')
        print(''.join(output_list))
    print()
