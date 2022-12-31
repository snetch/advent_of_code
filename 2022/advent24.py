# all coordinates are (y, x), where positive y is down on the drawn map
# for summation of blizzards, left=1, right=2, up=4, down=8

from sys import stdin


def blank_map(size_y, size_x):
    m = []
    for y in range(size_y):
        r = []
        for x in range(size_x):
            r.append(0)
        m.append(r)
    return(m)


def map_progress(old_map, size_y, size_x):
    new_map = blank_map(size_y, size_x)
    for y in range(size_y):
        for x in range(size_x):
            location = old_map[y][x]
            if location == 16:
                new_map[y][x] = 16
            else:
                dir = 0
                additive_direction_sign = 1
                while location>0:
                    if location % 2 == 1:
                        new_y = y + directions[dir][0]
                        new_x = x + directions[dir][1]
                        if old_map[new_y][new_x] == 16:  # thankfully no blizzards seem to want to go through the entry and exit gaps
                            new_y = y + overflow[dir][0]
                            new_x = x + overflow[dir][1]
                        new_map[new_y][new_x] += additive_direction_sign
                    dir += 1
                    additive_direction_sign *= 2
                    location //= 2
    return(new_map)


map = []
for line in stdin:
    row = []
    for c in line[:-1]:
        if c == "#":
            row.append(16)
        elif c == ".":
            row.append(0)
        elif c == "<":
            row.append(1)
        elif c == ">":
            row.append(2)
        elif c == "^":
            row.append(4)
        elif c == "v":
            row.append(8)
        else:
            print("wtf")
    map.append(row)

#for r in map:
#    print(r)
#print()

size_y = len(map)
size_x = len(map[0])
start = (0, 1)
end = (size_y-1, size_x-2)

# this list is left, right, up, down, wait
directions = [ (0,-1), (0,1), (-1,0), (1,0), (0,0) ]
# if a blizzard ends up in a wall because of directions, it will use overflow instead to teleport to the other size
overflow = [ (0,size_x-3), (0,3-size_x), (size_y-3,0), (3-size_y,0) ]


def run( start_location, end_location, start_time ):
    global map
    minute = start_time
    old_locations = [start_location]
    found = False
    while not found:
        minute += 1
#        print("current minute", minute, "size of locations", len(old_locations))
        map = map_progress(map, size_y, size_x)
        new_locations = []

        for loc in old_locations:
            for d in directions:
                new_y = loc[0]+d[0]
                new_x = loc[1]+d[1]
                if new_y>-1 and new_y<size_y and map[new_y][new_x] == 0:
                    if not (new_y, new_x) in new_locations:
                        new_locations.append( (new_y, new_x) )
                        if new_y == end_location[0] and new_x == end_location[1]:
                            found = True

        old_locations = new_locations

    return(minute)


t1 = run( start, end, 0)
t2 = run( end, start, t1)
t3 = run( start, end, t2)

print(t1, t2-t1, t3-t2, "total", t3)
