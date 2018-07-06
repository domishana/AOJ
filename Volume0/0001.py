# coding=utf-8


mountain_hills = [int(input()) for j in range(10)]
mountain_hills.sort()
mountain_hills.reverse()
mountain_hills = mountain_hills[:3]
for i in range(3):
    print(mountain_hills[i])
