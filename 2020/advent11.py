from sys import stdin

seats = []

for line in stdin:
    seats.append( list( "X" + line[:-1] + "X") ) # surround each row with dots
height = len(seats) + 2
width = len( seats[0] )

# surround the lines with a line of dots
seats.insert(0, ["X"]*width)
seats.append(["X"]*width)

def fill_round(s):
    new_seats = [ ["X"]*width for i in range(height) ]
    changed = False
    for i in range(1, height-1):
        for j in range(1, width-1):
            neighbors = [ s[i-1][j-1], s[i-1][j], s[i-1][j+1], s[i][j-1], s[i][j+1], s[i+1][j-1], s[i+1][j], s[i+1][j+1] ]
            if s[i][j] == "L" and "#" not in neighbors:
                new_seats[i][j] = "#"
                changed = True
            elif s[i][j] == "#" and neighbors.count("#")>3:
                new_seats[i][j] = "L"
                changed = True
            else:
                new_seats[i][j] = s[i][j]
    new_seats[0][0] = changed
    return(new_seats)

next = fill_round(seats)
while next[0][0]:
    seats = next
    next = fill_round(seats)
    for l in next:
        print(l)
    print()

print(sum( [x.count("#") for x in next] ))
