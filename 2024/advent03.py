from sys import stdin
import re

lines = ""
for line in stdin:
    print(line)
    lines += line

all_instructions = re.findall(   "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",   lines   )
print(all_instructions)

sum_of_muls_1 = 0
sum_of_muls_2 = 0
enabled = True
for i in all_instructions:
    if i[0:3] == "mul":
        a, b = i[4:-1].split(",")
        sum_of_muls_1 += int(a) * int(b)
        if enabled:
            sum_of_muls_2 += int(a) * int(b)
    elif i[0:4] == "do()":
        enabled = True
    elif i[0:7] == "don't()":
        enabled = False

print(sum_of_muls_1)
print(sum_of_muls_2)
