# coding=utf-8


if __name__ == '__main__':
    n = int(input())
    words_list = []
    for i in range(n):
        word = input()
        words_list.append(word)
    words_list.sort()
    print(words_list[0])
