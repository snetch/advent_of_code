from sys import stdin

elf_totals = []
current_elf = 0

for line in stdin:
    line = line[:-1]
    if line:
        current_elf += int(line)
    else:
        elf_totals += [current_elf]
        current_elf = 0

elf_totals.sort()
print(elf_totals[-3:], sum(elf_totals[-3:]))

# add one extra empty line to the end of the input file
