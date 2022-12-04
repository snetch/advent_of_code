# takes a wire in format like "R3,U5,L4"
# returns a list of tuples of coordinates that the wire covers
def generate_wire_tuples(wire):
    x, y, elapsed = 0, 0, 0
    wire_tuples = []
    for segment in wire:
        dir = segment[0]
        length = int(segment[1:])
        if dir == "R":
            for dx in range(1, length+1):
                wire_tuples.append( (x+dx, y, elapsed+dx) )
            x += dx
            elapsed += dx
        elif dir == "L":
            for dx in range(1, length+1):
                wire_tuples.append( (x-dx, y, elapsed+dx) )
            x -= dx
            elapsed += dx
        elif dir == "U":
            for dy in range(1, length+1):
                wire_tuples.append( (x, y+dy, elapsed+dy) )
            y += dy
            elapsed += dy
        elif dir == "D":
            for dy in range(1, length+1):
                wire_tuples.append( (x, y-dy, elapsed+dy) )
            y -= dy
            elapsed += dy
    return wire_tuples

wire1 = input().split(",")
wire2 = input().split(",")

wire1_tuples = generate_wire_tuples(wire1)
print("wire1_tuples length", len(wire1_tuples))
#print(wire1_tuples)
wire1_tuples.sort()

wire2_tuples = generate_wire_tuples(wire2)
print("wire2_tuples length", len(wire2_tuples))
#print(wire2_tuples)
wire2_tuples.sort()

i,j = 0,0
intersections = []
while i<len(wire1_tuples) and j<len(wire2_tuples):
    if wire1_tuples[i][0:2] < wire2_tuples[j][0:2]:
        i += 1
    elif wire1_tuples[i][0:2] > wire2_tuples[j][0:2]:
        j += 1
    else:
        intersections.append( (wire1_tuples[i][0],wire1_tuples[i][1],wire1_tuples[i][2]+wire2_tuples[j][2]) )
        i += 1
        j += 1
print("intersections complete")
#print(intersections)

min_dist = abs(intersections[0][0]) + abs(intersections[0][1])
min_steps = intersections[0][2]
for x,y,z in intersections:
    dist = abs(x)+abs(y)
    steps = z
    if dist < min_dist:
        min_dist = dist
    if steps < min_steps:
        min_steps = steps

print(min_dist)
print(min_steps)
