# coding=utf-8

sentences = []
while True:
    try:
        s = input()
        sentences.extend(s.lower())
    except EOFError:
        break

for i in range(ord('a'), ord('z')+1):
    print('{0} : {1}'.format(chr(i), sentences.count(chr(i))))
