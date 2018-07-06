# coding=utf-8
import math


a, b, C = map(int, input().split())
S = a*b*math.sin(math.pi*C/180)/2
h = 2*S/a
c_square = math.pow(a, 2) + math.pow(b, 2) - 2*a*b*math.cos(math.pi*C/180)
c = math.sqrt(c_square)
L = a+b+c
print(S, L, h)
