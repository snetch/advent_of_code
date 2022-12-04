from sys import stdin

containing_pairs = 0
overlapping_pairs = 0

for line in stdin:
    line = line[:-1]
    e1start, e1end, e2start, e2end = [   int(i)   for elf in line.split(",")   for i in elf.split("-")   ]

    if (e1start <= e2start) and (e1end >= e2end):
        print("elf 1 contains the other one:", e1start, e1end)
        containing_pairs += 1
    elif (e1start >= e2start) and (e1end <= e2end):
        print("elf 2 contains the other one:", e2start, e2end)
        containing_pairs += 1

    elif (e1start <= e2start) and (e2start <= e1end):
        print("elf 1 overlaps from the left")
        overlapping_pairs += 1
    elif (e2start <= e1start) and (e1start <= e2end):
        print("elf 2 overlaps from the left")
        overlapping_pairs += 1

print(containing_pairs, containing_pairs+overlapping_pairs)
