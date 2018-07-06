# coding=utf-8

pile = []
while True:
    order = input().split()
    if order[0] == 'quit':
        break
    if order[0] == 'push':
        pile.append(order[1])
    elif order[0] == 'pop':
        removed = pile.pop()
        print(removed)
