# coding=utf-8
import math


def distance(p1x: float, p1y: float, p2x: float, p2y: float) -> float:
    x_distance_square = math.pow(p2x - p1x, 2)
    y_distance_square = math.pow(p2y - p1y, 2)
    distance_between_2points = math.sqrt(x_distance_square + y_distance_square)
    return distance_between_2points


if __name__ == '__main__':
    x1, y1, x2, y2 = map(float, input().split())
    distance_1to2 = distance(x1, y1, x2, y2)
    print(distance_1to2)
