# coding=utf-8


class SetList:
    def __init__(self, number):
        self.number = number
        self.in_set = number
        self.same_child = []
        self.same_parent = -1

    def is_have_child(self):
        if self.same_child:
            return True
        return False

    def print_is_same(self, number1, number2, set_list):
        if is_in_same_list(number1, number2, set_list):
            print(1)
        else:
            print(0)

    def is_in_same_list(self, number1, number2, set_list):
        if set_list[number1].in_set == set_list[number2].in_set:
            return True
        return False

    def unite(self, number1, number2, s_list):
        if number1 > number2:
            n1, n2 = number2, number1
        else:
            n1, n2 = number1, number2

        s_list[n2].in_set = s_list[n1].in_set
        s_list[n2].same_parent = s_list[n1].number
        if s_list[n2].is_have_child():
            for elm in s_list[n2].same_child:
                s_list[elm].in_set = s_list[n1].in_set
                s_list[elm].same_parent = s_list[n1].number
        return s_list


if __name__ == '__main__':
    n, q = map(int, input().split())
    set_list = [SetList(j) for j in range(n)]

    for i in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            set_list = set_list.unite(x, y, set_list)
        elif com == 1:
            set_list.print_is_same(x, y, set_list)
