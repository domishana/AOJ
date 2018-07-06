# coding=utf-8

suits = {"S": 0, "H": 1, "C": 2, "D": 3}
tramp_list = [0 for i in range(52)]
n = int(input())

for j in range(n):
    card = input().split()
    card_number = suits[card[0]]*13 + int(card[1]) - 1
    tramp_list[card_number] = 1

for k in range(52):
    if tramp_list[k] == 0:
        suit_key = k // 13
        number_key = k % 13
        the_suit = 'undefined'

        for suit_name, suit_number in suits.items():
            if suit_number == suit_key:
                the_suit = suit_name

        print('{0} {1}'.format(the_suit, number_key+1))
