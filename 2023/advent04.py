from sys import stdin
import re

sum_part1 = 0
sum_part2 = 0
copies = [0]

for line in stdin:
    card_string, winning_string, have_string = re.split(': |:  | \| ', line)
    card = int( card_string.split()[1] )
    winning = winning_string.split()
    have = have_string.split()

    matches = 0
    for i in have:
        if i in winning:
            matches += 1

    if matches > 0:
        sum_part1 += 2 ** (matches-1)

    while len(copies) < card+matches+1:
        copies.append(1)
    for i in range(card+1, card+matches+1):
        copies[i] += copies[card]
    sum_part2 += copies[card]
#    print(card, copies[card], copies)

print(sum_part1)
print(sum_part2)
