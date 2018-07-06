# coding=utf-8

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    S = M
    for i in range(N):
        enter, exit = map(int, input().split())
        M += (enter-exit)
        if M < 0:
            print(0)
            break
        S = max(S, M)
    else:
        print(S)
