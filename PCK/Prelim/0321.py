# coding=utf-8


class ClubConflictException(Exception):
    pass


class Student:
    def __init__(self, number):
        self.name = number
        self.club = -1
        self.in_same_club = []

    def set_club(self, clb, order_from=None):
        if not self.is_belong():
            self.club = clb
            if not order_from is None:
                try:
                    self.in_same_club.remove(order_from)
                except ValueError:
                    pass
            self.synchronize_club()
        elif self.club == clb:
            if not order_from is None:
                try:
                    self.in_same_club.remove(order_from)
                except ValueError:
                    pass
        else:
            raise ClubConflictException

    def is_belong(self):
        if self.club == -1:
            return False
        return True

    def synchronize_club(self):
        if not self.in_same_club:
            pass
        else:
            to_synchro = self.in_same_club[:]
            for std in to_synchro:
                std.set_club(self.club, self)
                self.in_same_club.remove(std)


class Club:
    def __init__(self, number):
        self.name = number


class Commission:
    def __init__(self):
        self.student_list = []
        self.club_list = []

    def set_same_club(self, std1, std2):
        student1 = self.check_std(std1)
        student2 = self.check_std(std2)

        if student1.is_belong():
            student2.set_club(student1.club)
        elif student2.is_belong():
            student1.set_club(student2.club)
        else:
            student1.in_same_club.append(student2)
            student2.in_same_club.append(student1)

    def link_std_and_club(self, std, club):
        student = self.check_std(std)
        clb = self.check_club(club)

        student.set_club(clb)

    def check_std(self, std):
        if self.is_made_std(std):
            return self.search_list(std, self.student_list)
        return self.make_std(std)

    def check_club(self, club):
        if self.is_made_club(club):
            return self.search_list(club, self.club_list)
        return self.make_club(club)

    def search_list(self, element, org_list):
        list_to_dict = {elm.name: elm for elm in org_list}
        return list_to_dict[element]

    def is_made_std(self, std):
        std_n_list = [student.name for student in self.student_list]
        if std in std_n_list:
            return True
        return False

    def make_std(self, std):
        student = Student(std)
        self.student_list.append(student)
        return student

    def is_made_club(self, clb):
        club_n_list = [club.name for club in self.club_list]
        if clb in club_n_list:
            return True
        return False

    def make_club(self, club):
        clb = Club(club)
        self.club_list.append(clb)
        return clb


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    akira = Commission()
    for i in range(1, K+1):
        rtype, x1, x2 = map(int, input().split())

        if rtype == 1:
            try:
                akira.set_same_club(x1, x2)
            except ClubConflictException:
                print(i)
                break

        elif rtype == 2:
            try:
                akira.link_std_and_club(x1, x2)
            except ClubConflictException:
                print(i)
                break
    else:
        print(0)
