# coding=utf-8

if __name__ == '__main__':
    N = int(input())
    all_list = {i for i in range(1, N+1)}
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    C_list = list(map(int, input().split()))
    A_number = A_list[0]
    A_identity = set(A_list[1:])
    B_number = B_list[0]
    B_identity = set(B_list[1:])
    C_number = C_list[0]
    C_identity = set(C_list[1:])
    not_A_identity = all_list - A_identity

    cond1 = not_A_identity & C_identity
    cond2 = B_identity & C_identity

    suspected = cond1 | cond2
    print(len(suspected))
