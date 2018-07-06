# coding=utf-8

if __name__ == '__main__':
    N = int(input())
    product_dict = {}
    for i in range(N):
        p_name, number = input().split()
        number = int(number)
        try:
            product_dict[p_name] += number
        except KeyError:
            product_dict[p_name] = number
    view_list = product_dict.items()
    view_list = sorted(view_list, key=lambda x: (len(x[0]), x[0]))
    [print(' '.join(map(str, list_el))) for list_el in view_list]
