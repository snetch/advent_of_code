wait_start = int(input())
buses = [int(x) for x in input().split(",") if x != "x"]
min_wait = buses[0]
min_wait_ID = 0
for b in buses:
    missed_by = wait_start % b
    if missed_by > 0:
        wait = b-missed_by
        if wait < min_wait:
            min_wait = wait
            min_wait_ID = b
    else:
        min_wait = 0

print(min_wait, min_wait_ID, min_wait * min_wait_ID )
