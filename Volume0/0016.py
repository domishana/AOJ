# coding=utf-8
import math

x = 0
y = 0
direction = math.pi/2
while True:
    d, a = map(int, input().split(','))
    if d == 0 and a == 0:
        break
    x += d * math.cos(direction)
    y += d * math.sin(direction)
    direction -= a*math.pi/180
print('{0:.0f}'.format(math.modf(x)[1]))
print('{0:.0f}'.format(math.modf(y)[1]))
