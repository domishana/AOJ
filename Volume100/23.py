# coding=utf-8


if __name__ == '__main__':
    W = input().lower()
    sentence_list = []
    while True:
        word_line = input().split()
        if 'END_OF_TEXT' in word_line:
            sentence_end = word_line.index('END_OF_TEXT')
            sentence_list.extend(word_line[:sentence_end])
            break
        sentence_list.extend(word_line)
    sentence_list = [x.lower() for x in sentence_list]
    words_appearance = sentence_list.count(W)
    print(words_appearance)
