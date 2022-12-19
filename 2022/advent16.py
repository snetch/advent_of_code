from sys import stdin


class Valve:
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels


def lookup(name, valves):
    for v in valves:
        if v.name == name:
            return(v)


def lookup_index(name, valves):
    for i in range(len(valves)):
        if valves[i].name == name:
            return(i)


def parse_input_string(line):
    line = line.split(" ")
    return( Valve(
        line[1],
        int(  line[4][5:-1]  ),
        [ i[0:2] for i in line[9:] ]
    ) )


# assuming the current location is either "AA" or already opened
def walk( valves, location, released_so_far, time_left, opened):
    if time_left <= 1:
        return(released_so_far)

    global distances
    n = len(valves)

    current = lookup(location, valves)
    current_index = lookup_index(location, valves)
    best_so_far = released_so_far

#    print("Time left", time_left, "location", location, "current_index", current_index)

    # walk to other valves and open them
    for i in range(n):
        dest = valves[i]
        if dest.name != location and dest.flow_rate > 0 and not dest.name in opened:
            walk_time = distances[current_index][i]
            if walk_time+1 < time_left:
                opened.add(dest.name)
                new_time_left = time_left - walk_time - 1
                new_release = dest.flow_rate * new_time_left
                new_attempt = walk(valves, dest.name, released_so_far + new_release, new_time_left, opened)
                if new_attempt > best_so_far:
                    best_so_far = new_attempt
                opened.remove(dest.name)

    return(best_so_far)


valves = []
for line in stdin:
    valves.append( parse_input_string(line[:-1]) )

n = len(valves)

distances = []
for i in range(n):
    distances.append([ 30 for i in range(n)  ])
    distances[i][i] = 0

# floyd-warshall setup
for i in range(n):
    for j in valves[i].tunnels:
        j_index = lookup_index(j, valves)
        distances[i][j_index] = 1

# floyd-warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distances[i][k] + distances[k][j] < distances[i][j]:
                distances[i][j] = distances[i][k] + distances[k][j]

for i in distances:
    print(i)


#for i in range(31):
#    print(   i, walk( valves, "AA", 0, i, set(), "XX" )   )
print(   walk( valves, "AA", 0, 30, set() )   )
