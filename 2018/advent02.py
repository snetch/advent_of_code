twos = 0
threes = 0
all_lines = []

with open('advent02_input.txt') as f:
    for line in f:
        all_lines.append(line)
        freq = {}
        found2 = 0
        found3 = 0
        for c in line:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        for x in freq:
            if freq[x] == 2:
                found2 = 1
            elif freq[x] == 3:
                found3 = 1
        twos += found2
        threes += found3

print(twos, threes, twos*threes)



for i in all_lines:
    for j in all_lines:
        common = ""
        x = 0
        fails = 0
        while x<len(i) and fails<2:
            if i[x] == j[x]:
                common += i[x]
            else:
                fails += 1
            x += 1
        if fails == 1:
            print(i, j, common)
