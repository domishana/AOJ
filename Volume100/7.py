# coding=utf-8
a = []

while True:
    tmp = int(input())
    if tmp == 0:
        break
    a.append(tmp)

for i in range(len(a)):
    print('Case {0}: {1}'.format(i+1, a[i]))
