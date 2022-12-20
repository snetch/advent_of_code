jets = input()
current_jet = 0

shapes = [
["####"],
[".#.","###",".#."],
["###","..#","..#"],
["#","#","#","#"],
["##","##"]
]
current_shape = 0

# well[0] = floor, well[1] = first row
well = [
["#","#","#","#","#","#","#","#","#"],
["#",".",".",".",".",".",".",".","#"]
]
top = 0


def collision(well, shape, falling_x, falling_y, dirx, diry):
    found = False
    for y in range( len(shape) ):
        for x in range( len(shape[0]) ):
            if shape[y][x] == "#":
                if well[ falling_y + y + diry ][ falling_x + x + dirx ] == "#":
                    found = True
                    break
        if found:
            break
    return(found)


while current_shape < 2022:
    shape = shapes[current_shape % len(shapes)]
    spawn_x = 3
    spawn_y = top + 4

    spawn_y_top = spawn_y + len( shape ) - 1
    while len(well) < spawn_y_top+1:
        well.append( ["#",".",".",".",".",".",".",".","#"] )

    falling_x, falling_y = spawn_x, spawn_y
    while True:
        # push once with jet
        if jets[current_jet] == "<":
            dirx, diry = -1, 0
        else:
            dirx, diry = 1, 0

        if not collision(well, shape, falling_x, falling_y, dirx, diry):
#            print("Current jet #", current_jet, jets[current_jet], "no collision")
            falling_x += dirx
            falling_y += diry
#        else:
#            print("Current jet #", current_jet, jets[current_jet], "yes collision")

        current_jet = (current_jet+1) % len(jets)

        # drop once, possibly break
        dirx, diry = 0, -1

        if not collision(well, shape, falling_x, falling_y, dirx, diry):
#            print("dropped")
            falling_x += dirx
            falling_y += diry
        else:
#            print("not dropped")
            for y in range( len(shape) ):
                for x in range( len(shape[0]) ):
                    if shape[y][x] == "#":
                        well[ falling_y + y ][ falling_x + x ] = "#"
            top = max( top, falling_y + len(shape) - 1 )
            
            
#            temp = well[falling_y][falling_x]
#            well[falling_y][falling_x] = "O"
#            for i in well[::-1]:
#                print(i)
#            print("shape #", current_shape, "jet #", current_jet, "after converting")
#            print()
#            well[falling_y][falling_x] = temp



            break
    
    current_shape += 1

print(top)
