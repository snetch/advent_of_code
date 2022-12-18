from sys import stdin

SEARCH_MAX = 4000000   # 20 for the example, 4000000 for the real input
Y_LINE_TO_CHECK = SEARCH_MAX // 2

sensor_x = []
sensor_y = []
beacon_x = []
beacon_y = []
m_radius = []

for line in stdin:
    line = line[:-1].split(" ")
    sx = int( line[2][:-1].split("=")[1] )
    sy = int( line[3][:-1].split("=")[1] )
    bx = int( line[8][:-1].split("=")[1] )
    by = int( line[9]     .split("=")[1] )
    sensor_x.append(sx)
    sensor_y.append(sy)
    beacon_x.append(bx)
    beacon_y.append(by)
    m_radius.append(   abs(sx-bx) + abs(sy-by)   )



# generate tuples of x-coordinates that are covered by sensors for a certain y-coordinate
def generate_coverage_at_y(Y):

    global sensor_x, sensor_y, beacon_x, beacon_y, m_radius

    coverage = []

    for i in range( len(sensor_x) ):
        y_dist = abs( Y - sensor_y[i] )
        if y_dist <= m_radius[i]:
            coverage.append( (sensor_x[i] - m_radius[i] + y_dist, sensor_x[i] + m_radius[i] - y_dist) )

    return(coverage)



y_line_covered = generate_coverage_at_y(Y_LINE_TO_CHECK)
print(y_line_covered)

y_line_covered.sort()
print(y_line_covered)



# collapse multiple tuples of already pre-sorted coverage into one if they touch
def collapse(coverage):
    i = 0
    while i < len(coverage) - 1:
        if coverage[i][1] >= coverage[i+1][0] - 1:
            start = coverage[i][0]
            end = max( coverage[i][1], coverage[i+1][1] )
            coverage.pop(i)
            coverage.pop(i)
            coverage.insert( i, (start, end))
        else:
            i += 1



collapse(y_line_covered)
print(y_line_covered)

present_beacons = list(set(   [ beacon_x[i] for i in range(len(beacon_y)) if beacon_y[i] == Y_LINE_TO_CHECK ]   ))
present_beacons.sort()
print(present_beacons )



# split coverage based on existing beacons
def split_by_beacons(coverage, beacons):
    i = 0
    j = 0
    while i < len(coverage) and j < len(beacons):
        if beacons[j] < coverage[i][0]:
            j += 1
        elif beacons[j] == coverage[i][0]:
            coverage[i] = (coverage[i][0]+1, coverage[i][1])
            j += 1
        elif beacons[j] < coverage[i][1]:
            temp = coverage.pop(i)
            coverage.insert( i, (temp[0], beacons[j]-1) )
            coverage.insert( i+1, (beacons[j]+1, temp[1]) )
            i += 1
        elif beacons[j] == coverage[i][1]:
            coverage[i] = (coverage[i][0], coverage[i][1]-1)
            i += 1
            j += 1
        else:
            i += 1



split_by_beacons(y_line_covered, present_beacons)
print(y_line_covered)

total = 0
for i in y_line_covered:
    total += i[1]-i[0]+1
print(total)



# check if the already collapsed coverage leaves any gaps in the search area
def opening_in_coverage(coverage):
    i = 0
    for c in coverage:
        if c[1] < i:
            continue
        elif c[0] <= i and c[1] > i:
            i = c[1] + 1
        elif c[0] > i:
            return((True, i))
        if i > SEARCH_MAX:
            return((False, -1))



for y in range(0, SEARCH_MAX+1):
    y_line_covered = generate_coverage_at_y(y)
    y_line_covered.sort()
    collapse(y_line_covered)
    o = opening_in_coverage(y_line_covered)
    if o[0]:
        print(o[1], y, o[1]*4000000+y)
