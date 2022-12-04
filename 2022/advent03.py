from sys import stdin

priorities = 0
three_elves = []
badge_priorities = 0

def priority(c):
    if ord(i)<ord('a'):  # uppercase
        return( ord(i)-ord('A')+27 )
    # else lowercase
    return( ord(i)-ord('a')+1 )

for line in stdin:
    line = line[:-1]
    three_elves += [line]

    n = len(line)
    for i in line[:n//2]:
        if i in line[n//2:]:
            print(i)
            priorities += priority(i)
            break

    if len(three_elves) == 3:
        for i in three_elves[0]:
            if (i in three_elves[1]) and (i in three_elves[2]):
                print(i)
                badge_priorities += priority(i)
                break
        three_elves = []

print(priorities, badge_priorities)
