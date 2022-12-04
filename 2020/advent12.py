from sys import stdin
import math
"""
x, y, dir = 0, 0, 0

for line in stdin:
    action = line[0]
    value = int(line[1:-1])
    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    elif action == "L":
        dir += value
    elif action == "R":
        dir -= value
    elif action == "F":
        angle = dir/180*math.pi # dir is in degrees, angle is in radians for the math functions
        x += value * math.cos( angle )
        y += value * math.sin( angle )

print(x, y, abs(x)+abs(y))
"""


x, y, way_x, way_y = 0, 0, 10, 1

for line in stdin:
    action = line[0]
    value = int(line[1:-1])
    if action == "N":
        way_y += value
    elif action == "S":
        way_y -= value
    elif action == "E":
        way_x += value
    elif action == "W":
        way_x -= value
    elif action == "L":
        dist = math.sqrt(way_x * way_x + way_y * way_y)
        angle = math.atan(way_y / way_x)
        dir = angle*180/math.pi
        if way_x < 0:
            dir += 180

        dir += value
        angle = dir/180*math.pi
        way_x = dist * math.cos(angle)
        way_y = dist * math.sin(angle)
    elif action == "R":
        dist = math.sqrt(way_x * way_x + way_y * way_y)
        angle = math.atan(way_y / way_x)
        dir = angle*180/math.pi
        if way_x < 0:
            dir += 180

        dir -= value
        angle = dir/180*math.pi
        way_x = dist * math.cos(angle)
        way_y = dist * math.sin(angle)
    elif action == "F":
        x += way_x * value
        y += way_y * value
    print("command", action, value, "loc", x, y, "wp", way_x, way_y)

print(x, y, abs(x)+abs(y))
