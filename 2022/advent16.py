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
def walk( valves, locations, released_so_far, times_left, opened):
    next_worker_time = max(times_left)
    if next_worker_time <= 1:
        return(released_so_far)

    global distances
    n = len(valves)
    workers = len(locations)

#    currents = [ lookup(location, valves) for location in locations ]
    current_indexes = [ name_to_index[location] for location in locations ]
    best_so_far = released_so_far

    if next_worker_time == 26:
        print("Times left", times_left, "locations", locations, "current_indexes", current_indexes)

    # workers walk to other valves and open them
    for w in range(workers):
        if times_left[w] == next_worker_time:  # one worker (w) move is processed at a time even if both have the same time_left
            for i in worthy_valve_indexes:
                dest = valves[i]
                if (not dest.name in locations) and (not dest.name in opened):
                    walk_time = distances[current_indexes[w]][i]
                    if walk_time+1 < times_left[w]:
                        opened.add(dest.name)
                        new_time_left = times_left[w] - walk_time - 1
                        new_release = dest.flow_rate * new_time_left
                        
                        old_loc_w = locations[w]
                        locations[w] = dest.name
                        times_left[w] -= walk_time+1

                        new_attempt = walk(valves, locations, released_so_far + new_release, times_left, opened)
                        if new_attempt > best_so_far:
                            best_so_far = new_attempt

                        # put things back in place so that referred lists don't break for further calls
                        times_left[w] = next_worker_time
                        locations[w] = old_loc_w
                        opened.remove(dest.name)

    return(best_so_far)


valves = []
for line in stdin:
    valves.append( parse_input_string(line[:-1]) )

worthy_valve_indexes = [i for i in range(len(valves)) if valves[i].flow_rate > 0]
print(worthy_valve_indexes)
print()

n = len(valves)

distances = []
for i in range(n):
    distances.append([ 30 for i in range(n)  ])
    distances[i][i] = 0

name_to_index = {}
for i in valves:
    name_to_index[i.name] = lookup_index(i.name, valves)

print(name_to_index)
print()

# floyd-warshall setup
for i in range(n):
    for j in valves[i].tunnels:
        j_index = name_to_index[j]
        distances[i][j_index] = 1

# floyd-warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            if distances[i][k] + distances[k][j] < distances[i][j]:
                distances[i][j] = distances[i][k] + distances[k][j]

for i in distances:
    print(i)
print()

#for i in range(31):
#    print(   i, walk( valves, "AA", 0, i, set(), "XX" )   )

print(   walk( valves, ["AA"], 0, [30], set() )   )
print()

print(   walk( valves, ["AA", "AA"], 0, [26, 26], set() )   )
