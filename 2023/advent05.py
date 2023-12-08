class Map:
    def __init__(me, map_from, map_to, map_parts):
        me.map_from = map_from
        me.map_to = map_to
        me.map_parts = sorted( map_parts, key = lambda x: x[1] )

    def __str__(me):
        return( me.map_from + " " + me.map_to + " " + str(me.map_parts) )

    def next(me, x):
        if x < me.map_parts[0][1]:
            return(x)
        for p in me.map_parts:
            if x >= p[1] and x < p[1]+p[2]:
                return( x - p[1] + p[0] )
        return(x)

#    def next_interval(me, x_low, x_high):
#        current_from = x_low
#        current_map_part = 0
#        while current_from


seeds_input = [ int(i) for i in input().split()[1:] ]
print(seeds_input)
# part 1
seeds = sorted(seeds_input)
# part 2
#seeds = []
#for i in range( 0, len(seeds_input), 2):
#    for j in range(seeds_input[i], seeds_input[i]+seeds_input[i+1]):
#        seeds.append(j)

print(seeds)
line = input()

maps = []
last_map = False
while not last_map:
    map_from, map_to = input().split()[0].split("-to-")
    print( map_from, map_to )

    map_parts = []
    while True:
        try:
            line = input()
            if line == "":
                break
            map_parts.append( [ int(i) for i in line.split() ] )
        except EOFError:
            print("EOF")
            last_map = True
            break

    maps.append( Map(map_from, map_to, map_parts) )

pre_mapped = seeds
for m in maps:
    print(m)
    mapped = [ m.next(s) for s in pre_mapped ]
    print(m.map_to, mapped)
    pre_mapped = mapped

print( min(pre_mapped) )
