# coding=utf-8
while True:
    tmp = input().split()
    if tmp[1] == '?':
        break
    if tmp[1] == '+':
        print(int(tmp[0]) + int(tmp[2]))
    if tmp[1] == '-':
        print(int(tmp[0]) - int(tmp[2]))
    if tmp[1] == '*':
        print(int(tmp[0]) * int(tmp[2]))
    if tmp[1] == '/':
        print(int(tmp[0]) // int(tmp[2]))
