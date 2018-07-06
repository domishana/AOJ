# coding=utf-8


while True:
    cards = input()
    if cards == '-':
        break
    shuffle_numbers = int(input())
    for i in range(shuffle_numbers):
        shuffle_place = int(input())
        cards1 = cards[:shuffle_place]
        cards2 = cards[shuffle_place:]
        cards = cards2 + cards1
    print(cards)
