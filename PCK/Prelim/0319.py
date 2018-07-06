# coding=utf-8

if __name__ == '__main__':
    N = int(input())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)

    ctr = 1
    for element in score_list:
        if ctr > element:
            print(ctr-1)
            break
        ctr += 1
    else:
        print(ctr-1)
