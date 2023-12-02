from sys import stdin

id_sum = 0
power_sum = 0

thresholds = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for line in stdin:
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    id_string, sets_string = line.split(": ")
    game_id = int( id_string.split()[1] )

    sets = sets_string.split("; ")
    for s in sets:
        makeup = s.split(", ")
        for m in makeup:
            num, color = m.split()
            if int(num) > maxes[color]:
                maxes[color] = int(num)

    possible = True
    for color in thresholds.keys():
        if maxes[color] > thresholds[color]:
            possible = False
    if possible:
        id_sum += game_id

    power_sum += maxes["red"] * maxes["green"] * maxes["blue"]

print(id_sum)
print(power_sum)
