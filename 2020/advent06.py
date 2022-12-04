from sys import stdin

total = 0
total2 = 0
answers = []
current_group = []

for line in stdin:
    line = line[:-1]

    if len(line) > 0:
        for c in line:
            if c not in answers:
                answers.append(c)
        current_group.append(line) # for part 2
    else:
        total += len(answers)
        
        first = [c for c in current_group[0]] #individual letters of first person in the group
        for i in current_group[1:]:
            first = [point for point in i if point in first]
        total2 += len(first)

        print(len(answers), len(first))

        answers = []
        current_group = []

print(total, total2)
