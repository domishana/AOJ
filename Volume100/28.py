# coding=utf-8


def judge_battle(tcard: str, hcard: str) -> str:
    if tcard > hcard:
        return 'win'
    elif tcard == hcard:
        return 'equal'
    else:
        return 'lose'


if __name__ == '__main__':
    score_list = [0, 0]
    n = int(input())
    for i in range(n):
        card1, card2 = input().split()
        battle_result = judge_battle(card1, card2)
        if battle_result == 'win':
            score_list[0] += 3
        elif battle_result == 'equal':
            score_list[0] += 1
            score_list[1] += 1
        else:
            score_list[1] += 3
    print(' '.join(map(str, score_list)))
