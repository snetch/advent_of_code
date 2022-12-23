# all indices are in the order: y, then x
# increase in y is DOWN
dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
map = []
#x_size = 0

line = input()
while line != "":
    map.append(line)
#    if len(line) > x_size:
#        x_size = len(line)
    line = input()
y_size = len(map)

y = 0
x = map[0].index(".")
dir = 0

path = input()
while len(path) > 0:
    next_r = path.find("R")
    next_l = path.find("L")
    next_turn = len(path)
    if next_r > -1:
        next_turn = next_r
    if next_l > -1 and next_l < next_turn:
        next_turn = next_l
    print(next_r, next_l, next_turn, len(path))

    steps = int(path[:next_turn])
    path = path[next_turn:]
    while steps > 0:
        y_target = y + dirs[dir][0]
        x_target = x + dirs[dir][1]
        print("y, x, y_target, x_target, y_size", y, x, y_target, x_target, y_size)
        if y_target<0 or y_target>=y_size or x_target<0 or x_target>=len(map[y_target])   or   map[y_target][x_target] == " ":
            if dir == 0:  # right
                row = map[y_target]
                x_target = min( row.index("#"), row.index(".") )
            elif dir == 1:  # down
                column = "".join([  i[x_target] if len(i)>x_target else " " for i in map  ])
                y_target = min( column.index("#"), column.index(".") )
            elif dir == 2:  # left
                row = map[y_target]
                x_target = max( row.rindex("#"), row.rindex(".") )
            elif dir == 3:  # up
                column = "".join([  i[x_target] if len(i)>x_target else " " for i in map  ])
                y_target = max( column.rindex("#"), column.rindex(".") )
        if map[y_target][x_target] == "#":
            break
        y = y_target
        x = x_target
        steps -= 1

    if len(path)>0:
        if path[0] == "R":
            dir = (dir+1)%4
        elif path[0] == "L":
            dir = (dir-1)%4
        else:
            print("wtf no such turn direction", path[0])
        path = path[1:]

print(y+1, x+1, dir, (y+1)*1000 + (x+1)*4 + dir)
