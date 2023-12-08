part = 2

if part == 1:
    times = [ int(i) for i in input().split()[1:] ]
    distances = [ int(i) for i in input().split()[1:] ]
else:
    times = [ int( "".join(  input().split()[1:]) ) ]
    distances = [ int( "".join(  input().split()[1:]) ) ]

ways_total = 1
for race in range( len(times) ):
    for holding in range(1, times[race] // 2):
        if holding * (times[race]-holding) > distances[race]:
            ways = times[race] - 2*holding + 1
            ways_total *= ways
            break

print(ways_total)
