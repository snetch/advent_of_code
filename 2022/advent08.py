from sys import stdin

trees = [ line[:-1] for line in stdin ]
visible = []

rows = len(trees)
columns = len(trees[0])

for row in range( rows ):

    visible_row = []

    max = -1
    for column in range( columns ):
        tree = int(trees[row][column])
        if tree > max:
            max = tree
            visible_row.append( "Y" )
        else:
            visible_row.append( "N" )

    max = -1
    for column in range( columns-1, -1, -1 ):
        tree = int(trees[row][column])
        if tree > max:
            max = tree
            visible_row[column] = "Y"
    visible.append ( visible_row )

for column in range( columns ):

    max = -1
    for row in range(rows):
        tree = int(trees[row][column])
        if tree > max:
            max = tree
            visible[row][column] = "Y"

    max = -1
    for row in range(rows-1, -1, -1):
        tree = int(trees[row][column])
        if tree > max:
            max = tree
            visible[row][column] = "Y"

total_visible = 0
for i in visible:
    for j in i:
        if j == "Y":
            total_visible += 1
print(total_visible)



scenic_scores = []
best_scenic_score = -1

for row in range(rows):
    scenic_scores_one_row = []
    for column in range(columns):
        current = trees[row][column]

        view_left = 0
        view_right = 0
        view_up = 0
        view_down = 0

        i,j = row, column
        while j > 0:
            j -= 1
            view_left += 1
            if trees[i][j] >= current:
                break

        i,j = row, column
        while j < columns-1:
            j += 1
            view_right += 1
            if trees[i][j] >= current:
                break

        i,j = row, column
        while i > 0:
            i -= 1
            view_up += 1
            if trees[i][j] >= current:
                break

        i,j = row, column
        while i < rows-1:
            i += 1
            view_down += 1
            if trees[i][j] >= current:
                break

        scenic_score = view_left * view_right * view_up * view_down
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score
        scenic_scores_one_row.append(scenic_score)
    print(scenic_scores_one_row)
    scenic_scores.append(scenic_scores_one_row)

print(best_scenic_score)
