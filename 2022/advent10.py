from sys import stdin

X = 1
cycles = 0
leftover_addx = False
all_strengths = 0

while True:

    cycles += 1
    if cycles % 40 == 20:
        strength = cycles * X
#        print(strength)
        all_strengths += strength

    if abs(cycles % 40 - 1 - X) <= 1:
        print("#", end="")
    else:
        print(".", end="")

    if cycles % 40 == 0:
        print()

    if leftover_addx:  # second cycle of a previous addx command
        X += V
        leftover_addx = False
        continue

    try:
        line = input()
    except EOFError:
        print("EOF")
        break

    instr = line[:4]

    if instr == "addx":  
        leftover_addx = True
        V = int(line[5:])

print(all_strengths)
