# coding=utf-8

if __name__ == '__main__':
    S = int(input())
    while True:
        inp = input()
        if inp == '=':
            print(S)
            break
        elif inp == '+':
            inp_number = int(input())
            S += inp_number
        elif inp == '-':
            inp_number = int(input())
            S -= inp_number
        elif inp == '*':
            inp_number = int(input())
            S *= inp_number
        elif inp == '/':
            inp_number = int(input())
            S //= inp_number
