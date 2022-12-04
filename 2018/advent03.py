DIMENSION = 1000
fabric = [[0]*DIMENSION for i in range(DIMENSION)]
claims = []
with open('advent03_input.txt') as f:
#with open('input.txt') as f:
    for line in f:
        line_spl = line.split()
        id = line_spl[0][1:]
        start = line_spl[2][:-1].split(",")
        startx, starty = [int(i) for i in start]
        size = line_spl[3].split("x")
        sizex, sizey = [int(i) for i in size]
        claims.append([id, startx, starty, sizex, sizey])
#        print(start, size)
        for x in range(startx, startx + sizex):
            for y in range(starty, starty + sizey):
                fabric[x][y] += 1

total = 0
for x in range(DIMENSION):
    for y in range(DIMENSION):
        if fabric[x][y]>1:
            total += 1
print(total)
#for i in fabric:
#    print(i)

for i in claims:
    success = True
    for x in range(i[1], i[1]+i[3]):
        for y in range(i[2], i[2]+i[4]):
            if fabric[x][y] > 1:
                success = False
                break
        if not success:
            break
    if success:
        print(i[0])
