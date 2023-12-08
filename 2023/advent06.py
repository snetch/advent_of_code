times = [ int(i) for i in input().split()[1:] ]
distances = [ int(i) for i in input().split()[1:] ]

times.append(int( "".join(  [str(i) for i in times]  ) ))
distances.append(int( "".join(  [str(i) for i in distances]  ) ))

ways_total = 1
for race in range( len(times) ):
    for holding in range(1, times[race] // 2):
        if holding * (times[race]-holding) > distances[race]:
            ways = times[race] - 2*holding + 1
            ways_total *= ways
            print(ways, ways_total)
            break

print("Part 1: second to last line, end. Part 2: last line, start")
