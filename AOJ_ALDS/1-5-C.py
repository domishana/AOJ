# coding=utf-8
import math


def cut_into_three(start: list, end: list) -> list:
    x1 = (2*start[0]+end[0])/3
    y1 = (2*start[1]+end[1])/3
    mid_point1 = [x1, y1]

    x2 = (start[0]+2*end[0])/3
    y2 = (start[1]+2*end[1])/3
    mid_point2 = [x2, y2]

    points_list = [start, mid_point1, mid_point2, end]
    return points_list


def equil_triangle(point1: list, point2: list) -> list:
    cos60 = math.cos(math.pi / 3)
    sin60 = math.sin(math.pi / 3)

    x = (point2[0] - point1[0])*cos60 - (point2[1]-point1[1])*sin60 + point1[0]
    y = (point2[0] - point1[0])*sin60 + (point2[1]-point1[1])*cos60 + point1[1]

    return [x, y]


def make_projection(start: list, end: list) -> list:
    points_list = cut_into_three(start, end)
    projection_point = equil_triangle(points_list[1], points_list[2])
    points_list.insert(2, projection_point)
    return points_list


def koch_curve(start: list, end: list, number: int) -> list:
    if number == 0:
        return [start, end]
    else:
        points_list = make_projection(start, end)
        list1 = koch_curve(points_list[0], points_list[1], number-1)
        list2 = koch_curve(points_list[1], points_list[2], number-1)
        list3 = koch_curve(points_list[2], points_list[3], number-1)
        list4 = koch_curve(points_list[3], points_list[4], number-1)
        new_points_list = list1 + list2[1:] + list3[1:] + list4[1:]
        return new_points_list


if __name__ == '__main__':
    n = int(input())
    p1 = [0, 0]
    p2 = [100, 0]
    fractal_points = koch_curve(p1, p2, n)
    for i in fractal_points:
        print(' '.join(map(str, i)))
