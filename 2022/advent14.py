from sys import stdin

# small limits for the example
#MIN_X = 490
#MAX_X = 510
#MAX_Y = 15

# fits the pile, and fits on my screen
MIN_X = 320
MAX_X = 680
MAX_Y = 200

sand_spawn_x = 500
sand_spawn_y = 0

map = []
for i in range(MAX_Y):
    map.append(["." for i in range(MAX_X)])

MAX_Y = 0  # reusing for the actual floor for part 2

for line in stdin:
    line = line[:-1].split(" -> ")

    startx, starty = line[0].split(",")
    startx, starty = int(startx), int(starty)
    if starty > MAX_Y:
        MAX_Y = starty
    for i in range(1, len(line)):
        endx, endy = line[i].split(",")
        endx, endy = int(endx), int(endy)
        if endy > MAX_Y:
            MAX_Y = endy
        dirx = 0 if endx == startx else (endx-startx)//abs(endx-startx)
        diry = 0 if endy == starty else (endy-starty)//abs(endy-starty)

        map[starty][startx] = "#"
        while startx != endx or starty != endy:
            startx += dirx
            starty += diry
            map[starty][startx] = "#"

MAX_Y += 2
for i in range(  len(map[MAX_Y])  ):
    map[MAX_Y][i] = "#"
while len(map) > MAX_Y+1:
    map.pop()

for i in map:
    print("".join(i[MIN_X:MAX_X]))
print()


sand_count = 0
found_floor = False

while True:
    sand_count += 1
    x = sand_spawn_x
    y = sand_spawn_y

    while True:
        if map[y+1][x] == ".":
            y += 1
        elif map[y+1][x-1] == ".":
            x -= 1
            y += 1
        elif map[y+1][x+1] == ".":
            x += 1
            y += 1
        else:
            break

    map[y][x] = "o"

    if y == MAX_Y-1 and not found_floor:
        found_floor = True
        for i in map:
            print("".join(i[MIN_X:MAX_X]))
        print()

        print(sand_count-1)

    if y == 0:
        for i in map:
            print("".join(i[MIN_X:MAX_X]))
        print()

        print(sand_count)
        break
