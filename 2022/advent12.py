from sys import stdin

map = []

row = 0
for line in stdin:
    line = line[:-1]

    elevations_row = []
    column = 0
    for i in line:
        if i == "S":
            startr = row
            startc = column
            elevations_row.append("a")
        elif i == "E":
            endr = row
            endc = column
            elevations_row.append("z")
        else:
            elevations_row.append(i)
        column += 1
    map.append(elevations_row)
    row += 1

# after that, row and column are left at the number of rows and columns

for i in map:
    print(i)

def steps_to_goal_from(startr, startc):

    global map, row, column, endr, endc

    # prepare the blank visited grid
    visited = []
    for i in range(row):
        visited_row = []
        for j in range(column):
            visited_row.append(False)
        visited.append(visited_row)
    visited[startr][startc] = True

    steps = 0
    before_step = [(startr, startc)]
    after_step = []

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while True:
        steps += 1
        for i in before_step:
            r, c = i
            for d in directions:
                r2 = r+d[0]
                c2 = c+d[1]
                if r2 >= 0 and r2 < row and c2 >= 0 and c2 < column:
                    if (not visited[r2][c2]) and ord(map[r2][c2]) <= ord(map[r][c])+1:
                        after_step.append((r2, c2))
                        visited[r2][c2] = True
                        if r2 == endr and c2 == endc:
                            return(steps)
#        print(steps, after_step)
        before_step = after_step
        after_step = []
        if len(before_step) == 0:
            break

min_steps = steps_to_goal_from(startr, startc)
print(min_steps)

for i in range(row):
    for j in range(column):
        if map[i][j] == "a":
            current = steps_to_goal_from(i,j)
#            print(current, i, j)
            if current != None and current < min_steps:
                min_steps = current
                print(min_steps, i, j)
